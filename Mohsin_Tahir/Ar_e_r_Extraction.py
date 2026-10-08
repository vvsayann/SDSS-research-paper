import numpy as np
from astropy.io import fits

file_path = "../Spectrum/spec-0266-51630-0098.fits"

try:
    with fits.open(file_path) as hdul:
        metadata = hdul[2].data

        # 1. Calculate Photometric Error (u, g, r, i, z)
        ivar = metadata['SPECTROFLUX_IVAR'][0]
        photo_error = np.zeros_like(ivar)
        valid_pixels = ivar > 0
        photo_error[valid_pixels] = 1.0 / np.sqrt(ivar[valid_pixels])



        print(f"--- Data for spec-0266-51630-0098.fits ---")
        print(f"Photometric Error (u, g, r, i, z): {photo_error}")


except Exception as e:
    print(f"An error occurred: {e}")