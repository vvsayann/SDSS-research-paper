"""Export SDSS COADD and LAMOST spectra, one wavelength sample per CSV row.

Usage: .venv/Scripts/python.exe export_spectra_csv.py [Spectrum_folder]
Each spectral column contains a single number. Native FITS flux units remain.
This extracts existing data; it does not fit parameters or preprocess spectra.
"""

import argparse
import csv
import json
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
from astropy.io import fits


FIELDS = [
    "filename", "survey", "obsid", "observation_key", "ra_deg", "dec_deg", "class", "subclass",
    "teff_K", "teff_err_K", "logg", "logg_err", "parameter_source",
    "parameter_status", "n_pixels", "pixel_index", "wavelength_unit", "wavelength_medium",
    "flux_unit", "inverse_variance_unit", "wavelength", "flux",
    "inverse_variance", "and_mask", "or_mask",
]


def clean(value):
    if isinstance(value, bytes):
        return value.decode().strip()
    if isinstance(value, str):
        return value.strip()
    return value.item() if isinstance(value, np.generic) else value


def extract(path):
    row = dict.fromkeys(FIELDS, "")
    row.update(filename=path.name, wavelength_unit="Angstrom",
               parameter_status="missing_in_fits")
    with fits.open(path) as hd:
        header = hd[0].header
        if "COADD" in hd:
            data = hd["COADD"].data
            obj = hd["SPECOBJ"].data[0]
            wavelength = 10.0 ** np.asarray(data["loglam"], dtype=np.float64)
            flux, ivar = data["flux"], data["ivar"]
            and_mask, or_mask = data["and_mask"], data["or_mask"]
            row.update(
                survey="SDSS", obsid=str(obj["SPECOBJID"]),
                ra_deg=clean(obj["PLUG_RA"]), dec_deg=clean(obj["PLUG_DEC"]),
                **{"class": clean(obj["CLASS"]), "subclass": clean(obj["SUBCLASS"])},
                flux_unit=header.get("BUNIT", "unspecified_in_fits"),
            )
            if "ELODIE_TEFF" in obj.array.names and "ELODIE_LOGG" in obj.array.names:
                teff, logg = float(obj["ELODIE_TEFF"]), float(obj["ELODIE_LOGG"])
                row.update(parameter_source="SPECOBJ:ELODIE_TEFF,ELODIE_LOGG",
                           parameter_status="pipeline_estimates_unvalidated")
                row["teff_K"] = teff if np.isfinite(teff) and teff > 0 else ""
                row["logg"] = logg if np.isfinite(logg) and logg > -100 else ""
        elif header.get("TELESCOP", "").strip() == "LAMOST" and hd[0].data.shape[0] == 5:
            flux, ivar, wavelength, and_mask, or_mask = hd[0].data
            row.update(
                survey="LAMOST", obsid=str(header["OBSID"]),
                ra_deg=header.get("RA", ""), dec_deg=header.get("DEC", ""),
                **{"class": header.get("CLASS", ""), "subclass": header.get("SUBCLASS", "")},
                flux_unit=header.get("BUNIT", "unspecified_in_fits"),
            )
        else:
            raise ValueError(f"Unsupported FITS layout: {path}")

        arrays = dict(wavelength=wavelength, flux=flux, inverse_variance=ivar,
                      and_mask=and_mask, or_mask=or_mask)
        if any(np.ndim(a) != 1 or len(a) != len(flux) for a in arrays.values()):
            raise ValueError(f"Inconsistent spectral array dimensions: {path}")
        if not np.all(np.isfinite(wavelength)) or not np.all(np.diff(wavelength) > 0):
            raise ValueError(f"Invalid wavelength grid: {path}")
        row.update(n_pixels=len(flux),
                   wavelength_medium="vacuum" if header.get("VACUUM") is True else "unspecified_in_fits",
                   inverse_variance_unit="1/(native_flux_unit)^2")
        # Copy arrays before the FITS file closes.
        row.update({name: np.array(values, copy=True) for name, values in arrays.items()})
        row["observation_key"] = row["survey"] + ":" + row["obsid"]
    return row


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("folder", nargs="?", type=Path,
                        default=Path(__file__).resolve().parent / "Spectrum")
    args = parser.parse_args()
    files = sorted(p for p in args.folder.iterdir()
                   if p.is_file() and p.name.lower().endswith((".fits", ".fit", ".fits.gz")))
    if not files:
        raise ValueError(f"No FITS files found in {args.folder}")
    output = args.folder / "spectra_parameters_pixels.csv"
    temporary = output.with_suffix(".csv.tmp")
    counts, status = Counter(), Counter()
    pixels = 0
    try:
        with temporary.open("w", newline="", encoding="utf-8") as stream:
            writer = csv.DictWriter(stream, fieldnames=FIELDS)
            writer.writeheader()
            for path in files:
                row = extract(path)
                arrays = {key: row.pop(key) for key in
                          ["wavelength", "flux", "inverse_variance", "and_mask", "or_mask"]}
                for index in range(row["n_pixels"]):
                    sample = dict(row, pixel_index=index)
                    for key, values in arrays.items():
                        value = values[index]
                        sample[key] = (int(value) if key.endswith("mask") else float(value)) if np.isfinite(value) else ""
                    writer.writerow(sample)
                counts[row["survey"]] += 1
                status[row["parameter_status"]] += 1
                pixels += row["n_pixels"]
        temporary.replace(output)
    finally:
        if temporary.exists():
            temporary.unlink()
    summary = dict(generated_at=datetime.now(timezone.utc).isoformat(),
                   generator=Path(__file__).name, output=str(output.resolve()),
                   spectrum_count=len(files), pixel_count=pixels, data_rows=pixels,
                   layout="One wavelength sample per row; zero-based pixel_index",
                   surveys=dict(counts), parameter_status=dict(status),
                   parameter_uncertainties="Not present in source FITS files; blank",
                   processing="Extraction only; native flux and inverse variance retained")
    output.with_suffix(".summary.json").write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
