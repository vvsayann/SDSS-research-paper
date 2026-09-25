import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits

FITS_FILE =  r'C:\Users\yoboy\Desktop\SDSS-research-paper\Spectrum\spec-0267-51608-0271.fits'
hdul = fits.open(FITS_FILE)

# --- Load data -------------------------------------------------------------
with fits.open(FITS_FILE) as hdul:
    spec = hdul[1].data      # COADD: flux, loglam, ivar, model, ...
    specobj = hdul[2].data[0]  # SPECOBJ: one row of metadata

wave = 10 ** spec["loglam"]  # Angstrom (vacuum)
flux = spec["flux"]          # 1e-17 erg/cm^2/s/Ang
model = spec["model"]
good = spec["ivar"] > 0      # drop bad pixels

# --- S/N values ------------------------------------------------------------
bands = ["u", "g", "r", "i", "z"]
band_centers = [3543, 4770, 6231, 7625, 9134]  # SDSS effective wavelengths (Ang)
sn_bands = specobj["SN_MEDIAN"]
sn_all = specobj["SN_MEDIAN_ALL"]

# --- Plot ------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(wave[good], flux[good], color="steelblue", lw=0.8, label="Flux")
ax.plot(wave, model, color="tomato", lw=0.8, alpha=0.7, label="Best-fit model")

# Mark each band's center and label it with its median S/N (labels sit above the axes)
xmin, xmax = wave.min(), wave.max()
for b, wc, sn in zip(bands, band_centers, sn_bands):
    x = min(max(wc, xmin), xmax)  # u-band center lies just below the data range
    if xmin < wc < xmax:
        ax.axvline(wc, color="gray", ls=":", lw=0.8)
    ha = "left" if wc <= xmin else ("right" if wc >= xmax - 200 else "center")
    ax.text(x, 1.01, f"{b}: S/N={sn:.1f}", transform=ax.get_xaxis_transform(),
            ha=ha, va="bottom", fontsize=9)

# Summary box with all SN_MEDIAN values
lines = [f"SN_MEDIAN_ALL = {sn_all:.2f}"] + [
    f"SN_MEDIAN[{b}] = {sn:.2f}" for b, sn in zip(bands, sn_bands)
]
ax.text(
    0.98, 0.95, "\n".join(lines), transform=ax.transAxes,
    ha="right", va="top", fontsize=10, family="monospace",
    bbox=dict(boxstyle="round", facecolor="white", edgecolor="gray", alpha=0.9),
)

ax.set_xlabel("Wavelength (Å)")
ax.set_ylabel(r"Flux ($10^{-17}$ erg cm$^{-2}$ s$^{-1}$ Å$^{-1}$)")
ax.set_title(f"{specobj['CLASS']} ({specobj['SUBCLASS']}) | Plate {specobj['PLATE']}, "
             f"MJD {specobj['MJD']}, Fiber {specobj['FIBERID']}", pad=28)
ax.set_xlim(wave.min(), wave.max())
ax.legend(loc="lower left")
fig.tight_layout()
plt.show()