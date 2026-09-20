
import csv
import sys
from pathlib import Path

import numpy as np
from astropy.io import fits

# Folder to scan. You can also pass a different folder on the command line:
#     python export_sn_csv.py "D:\\other\\folder"
DEFAULT_FOLDER = r"C:\Users\yoboy\Desktop\SDSS-research-paper-\Spectrum"
FOLDER = Path(sys.argv[1] if len(sys.argv) > 1 else DEFAULT_FOLDER)
OUT_CSV = FOLDER / "sn_values.csv"

BANDS = ["u", "g", "r", "i", "z"]
COLUMNS = (
    ["filename", "plate", "mjd", "fiberid", "class", "subclass", "z",
     "sn_median_all"]
    + [f"sn_median_{b}" for b in BANDS]
    + ["sn_pixel_median", "plate_sn2"]
)


def to_str(value):
    """Clean up FITS string values (they are often space-padded)."""
    return value.strip() if isinstance(value, str) else value


def read_one(path):
    """Return one CSV row (dict) for a single spectrum file."""
    with fits.open(path) as hdul:
        coadd = hdul[1].data
        obj = hdul[2].data[0]

        flux, ivar = coadd["flux"], coadd["ivar"]
        good = ivar > 0
        pixel_sn = float(np.median(flux[good] * np.sqrt(ivar[good]))) if good.any() else np.nan

        row = {
            "filename": path.name,
            "plate": obj["PLATE"],
            "mjd": obj["MJD"],
            "fiberid": obj["FIBERID"],
            "class": to_str(obj["CLASS"]),
            "subclass": to_str(obj["SUBCLASS"]),
            "z": obj["Z"],
            "sn_median_all": obj["SN_MEDIAN_ALL"],
            "sn_pixel_median": pixel_sn,
            "plate_sn2": obj["PLATESN2"],
        }
        for b, sn in zip(BANDS, obj["SN_MEDIAN"]):
            row[f"sn_median_{b}"] = sn
    return row


def main():
    if not FOLDER.is_dir():
        print(f"Folder not found: {FOLDER}")
        return

    files = sorted(
        p for p in FOLDER.iterdir()
        if p.is_file() and p.name.lower().endswith((".fits", ".fit", ".fits.gz"))
    )
    if not files:
        print(f"No FITS files found in {FOLDER}")
        return

    rows = []
    for path in files:
        try:
            rows.append(read_one(path))
            print(f"OK      {path.name}")
        except Exception as exc:  # keep going if one file is unreadable
            print(f"SKIPPED {path.name}: {exc}")

    with open(OUT_CSV, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=COLUMNS)
        writer.writeheader()
        for row in rows:
            writer.writerow({k: (f"{v:.6g}" if isinstance(v, (float, np.floating)) else v)
                             for k, v in row.items()})

    print(f"\nWrote {len(rows)} row(s) to {OUT_CSV}")


if __name__ == "__main__":
    main()