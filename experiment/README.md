# B-star SLAM experiment

This experiment estimates effective temperature (Teff in K) and surface gravity (log g in dex) from LAMOST low-resolution B-star spectra. Input FITS files need the five-row LAMOST primary HDU and a usable Z redshift header.

## Set up on Windows

From this folder in PowerShell, use Python 3.14.5, the version used to verify this experiment.

```powershell
py -3.14 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r .\requirements.txt
```

## Predict with the included model

```powershell
.\.venv\Scripts\python.exe .\train_b_stars.py --predict .\data\Spectra\spec-56293-VB073N23V2_sp14-014.fits
```

The example is a held-out star. The bundled model returns Teff of about 13,309 K and log g of 4.000 dex. Replace the example path with your FITS path, or pass multiple paths after `--predict`.

## Reproduce the fit

```powershell
.\.venv\Scripts\python.exe .\train_b_stars.py --model .\b_star_slam_retrained.joblib
```

The included catalog and 107 spectra reproduce the 85-star training split and 22-star holdout. The holdout is grouped by star ID. The original fit had a held-out mean absolute error of 1,498 K for Teff and 0.264 dex for log g against the catalog labels. Catalog provenance and measurement references are recorded in `data/Spectra/fits_parameters_only.csv`.

Pass `--model .\b_star_slam_retrained.joblib` with `--predict` to use the reproduced fit. The supplied model is serialized with joblib and uses the bundled `slam` package.
