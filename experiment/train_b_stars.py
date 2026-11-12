"""Train SLAM on the local LAMOST B-star sample and estimate stellar labels."""

import argparse
from pathlib import Path

import numpy as np
import pandas as pd
from astropy.io import fits
from scipy.ndimage import median_filter
from sklearn.model_selection import GroupShuffleSplit

from slam.slam import Slam


PROJECT_ROOT = Path(__file__).resolve().parent
LABELS = ["teff_K", "logg"]


def read_spectra(paths, wave):
    """Return continuum-normalized spectra on the model's rest-frame grid."""
    fluxes, inverse_variances = [], []
    for path in paths:
        with fits.open(path) as hdul:
            data = hdul[0].data
            if data is None or data.ndim != 2 or data.shape[0] != 5:
                raise ValueError(f"{path}: expected a five-row LAMOST FITS primary HDU")
            try:
                redshift = float(hdul[0].header["Z"])
            except (KeyError, TypeError, ValueError) as error:
                raise ValueError(f"{path}: missing or invalid FITS redshift Z") from error
            if not np.isfinite(redshift) or redshift <= -1:
                raise ValueError(f"{path}: missing or invalid FITS redshift Z")

            flux, ivar, observed_wave, _, or_mask = data.astype(float)
        rest_wave = observed_wave / (1 + redshift)
        if not np.isfinite(rest_wave).all() or not np.all(np.diff(rest_wave) > 0):
            raise ValueError(f"{path}: wavelengths must be finite and increasing")
        good = np.isfinite(flux) & np.isfinite(ivar) & (ivar > 0) & (or_mask == 0)
        if np.count_nonzero(good) < 2:
            raise ValueError(f"{path}: too few usable input pixels")

        # Fill gaps for continuum estimation and give those pixels zero weight.
        resampled = np.interp(wave, rest_wave[good], flux[good])
        valid = np.interp(wave, rest_wave, good, left=0, right=0) == 1
        weight = np.interp(wave, rest_wave, np.where(good, ivar, 0.0))
        continuum = median_filter(resampled, size=101, mode="nearest")
        valid &= np.isfinite(continuum) & (continuum > 0)
        if np.count_nonzero(valid) < wave.size // 2:
            raise ValueError(f"{path}: fewer than half the model pixels are usable")

        normalized = np.divide(resampled, continuum, out=np.ones_like(wave), where=valid)
        fluxes.append(normalized)
        inverse_variances.append(np.where(valid, weight * continuum**2, 0.0))

    return np.stack(fluxes), np.stack(inverse_variances)


def estimate_labels(model, flux, ivar):
    initial = model.predict_labels_quick(flux, ivar, n_jobs=1)
    estimated = model.predict_labels_multi(initial, flux, ivar, n_jobs=1)
    if not np.isfinite(estimated).all():
        raise ValueError("SLAM could not estimate finite labels for the input spectra.")
    return estimated


def train(data_dir, model_path, overwrite):
    if model_path.exists() and not overwrite:
        raise FileExistsError(f"{model_path} already exists. Use --overwrite to retrain.")

    catalog = pd.read_csv(data_dir / "fits_parameters_only.csv")
    labels = catalog[LABELS].to_numpy(dtype=float)
    if not np.isfinite(labels).all() or catalog["star_id"].isna().any():
        raise ValueError("Every training row needs finite labels and a star_id.")

    wave = np.arange(3900.0, 6801.0, 2.0)
    flux, ivar = read_spectra((data_dir / name for name in catalog["filename"]), wave)
    split = GroupShuffleSplit(n_splits=1, test_size=0.2, random_state=42)
    train_rows, test_rows = next(split.split(flux, groups=catalog["star_id"]))
    model = Slam(wave, flux[train_rows], ivar[train_rows], labels[train_rows])
    model.train_pixels(method="simple", C=2.0, epsilon=0.1, gamma=1.0,
                       cv=1, n_jobs=1, verbose=0)

    test_flux, test_ivar = flux[test_rows], ivar[test_rows]
    reconstructed = model.predict_spectra(labels[test_rows], n_jobs=1)
    valid = test_ivar > 0
    flux_rmse = np.sqrt(np.mean((reconstructed[valid] - test_flux[valid])**2))
    estimated = estimate_labels(model, test_flux, test_ivar)
    teff_mae, logg_mae = np.abs(estimated - labels[test_rows]).mean(axis=0)
    if not np.isfinite([flux_rmse, teff_mae, logg_mae]).all():
        raise ValueError("Held-out evaluation returned a non-finite metric.")

    print(f"Training spectra: {len(train_rows)} | Held-out spectra: {len(test_rows)}")
    print(f"Held-out normalized flux RMSE: {flux_rmse:.4f}")
    print(f"Held-out label MAE: Teff {teff_mae:,.0f} K | log g {logg_mae:.3f} dex")
    model.save_dump(model_path, overwrite=overwrite, compress=3)
    print(f"Saved model to {model_path.resolve()}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data-dir", type=Path, default=PROJECT_ROOT / "data" / "Spectra")
    parser.add_argument("--model", type=Path, default=PROJECT_ROOT / "b_star_slam.joblib")
    parser.add_argument("--overwrite", action="store_true", help="replace the saved model")
    parser.add_argument("--predict", type=Path, nargs="+", metavar="FITS",
                        help="load the model and estimate labels for these LAMOST FITS files")
    args = parser.parse_args()

    try:
        if args.predict:
            model = Slam.load_dump(args.model)
            flux, ivar = read_spectra(args.predict, model.wave)
            for path, (teff, logg) in zip(args.predict, estimate_labels(model, flux, ivar)):
                print(f"{path.name}: Teff = {teff:,.0f} K, log g = {logg:.3f} dex")
        else:
            train(args.data_dir, args.model, args.overwrite)
    except (OSError, ValueError) as error:
        parser.exit(1, f"{parser.prog}: {error}\n")


if __name__ == "__main__":
    main()
