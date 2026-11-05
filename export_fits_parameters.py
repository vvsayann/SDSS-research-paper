"""Export existing stellar parameters for FITS files directly in Spectrum.

One row per observed spectrum. Missing values remain blank. Existing SDSS
ELODIE estimates are explicitly marked as unvalidated pipeline estimates.
"""

import csv
from pathlib import Path

from export_spectra_csv import extract


FIELDS = [
    "filename", "survey", "obsid", "observation_key", "ra_deg", "dec_deg",
    "class", "subclass", "teff_K", "teff_err_K", "logg", "logg_err",
    "parameter_source", "parameter_status",
]


def main():
    folder = Path(__file__).resolve().parent / "Spectrum"
    files = sorted(p for p in folder.iterdir() if p.is_file()
                   and p.name.lower().endswith((".fits", ".fit", ".fits.gz")))
    if not files:
        raise ValueError(f"No FITS files found in {folder}")
    output = folder / "fits_parameters_only.csv"
    temporary = output.with_suffix(".csv.tmp")
    populated = 0
    try:
        with temporary.open("w", newline="", encoding="utf-8") as stream:
            writer = csv.DictWriter(stream, fieldnames=FIELDS)
            writer.writeheader()
            for path in files:
                data = extract(path)
                row = {key: data[key] for key in FIELDS}
                writer.writerow(row)
                populated += row["teff_K"] != "" and row["logg"] != ""
        temporary.replace(output)
    finally:
        if temporary.exists():
            temporary.unlink()
    print(f"Saved {len(files)} spectra to {output}")
    print(f"{populated} with existing pipeline temperature/gravity; {len(files)-populated} without.")


if __name__ == "__main__":
    main()
