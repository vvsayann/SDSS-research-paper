## 15/10/26

from this code:
```python
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

```
### we get output:
--- Data for spec-0266-51630-0098.fits ---
Photometric Error (u, g, r, i, z): [1.0027971  0.556955   0.7914383  0.94669473 1.3628478 ]

#### explanation:

o extract the required data, we first created a Python script named `Ar_e_r_Extraction.py`. Within the standard SDSS `.fits` files, the direct photometric error is not provided in the `HDU[2]` metadata table.
Instead, the pipeline stores the uncertainty as Inverse Variance (`SPECTROFLUX_IVAR`). We mathematically calculate the exact photometric error from this array using the formula $\text{Error} = 1 / \sqrt{\text{IVAR}}$. Furthermore, 
because physical interstellar reddening ($E(B-V)$) is entirely absent from these specific spectroscopic files,