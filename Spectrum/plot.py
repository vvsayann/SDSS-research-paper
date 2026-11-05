
import os
from astropy.io import fits
import numpy as np
import matplotlib.pyplot as plt

filename = r'C:\Users\yoboy\Desktop\SDSS-research-paper\Spectrum\spec-56293-VB073N23V2_sp01-177.fits'

# Open FITS file
with fits.open(filename) as hdul:
    header = hdul[0].header

    # Data stored in primary HDU (index 0)
    flux_raw = hdul[0].data[0]
    inverse_variance = hdul[0].data[1]
    wavelength = hdul[0].data[2]
    and_mask = hdul[0].data[3]
    or_mask = hdul[0].data[4]

def vacuum_to_air(wavelength: np.ndarray) -> np.ndarray:
    term1 = 5.792105E-2 / (238.0185 - (1.0E4 / wavelength)**2)
    term2 = 1.67917E-3 / (57.362 - (1.0E4 / wavelength)**2)
    air = wavelength / (1.0 + term1 + term2)
    return air

# Convert vacuum wavelengths to air wavelengths
wavelength_air = vacuum_to_air(wavelength)

# Convert flux to physical units
# Assumes FITS flux is in units of 1e-17 erg/s/cm^2/A
flux = flux_raw * 1e-17

print("Wavelength (A):", wavelength_air)
print("Flux (erg/s/cm^2/A):", flux)

# Plot spectrum
plt.figure(figsize=(15, 10))
plt.plot(wavelength_air, flux, color='red', lw=0.5)


plt.xlabel('Wavelength (Angstrom)')
plt.ylabel('Flux (erg/s/cm²/Å)')
plt.title('Flux vs Wavelength')
plt.grid(alpha=0.5)
plt.tight_layout()
plt.show()
