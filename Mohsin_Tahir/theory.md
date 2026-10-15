# Theory Finding Log

## Date: 09/1/26
### Topic: Classification of Hot O-Type Stars (O2-O3)

**The Problem (Martins 2018):** https://arxiv.org/pdf/1805.08267
- Martins (2018) created the standard quantitative criteria using the **He I 4471 / He II 4542 ratio** to find the temperature.
- **BUT:** This method fails for the hottest O-type stars (O2, O3).
- **Why it fails:** At these extreme temperatures (45,000K+), stellar winds are incredibly powerful. 
- The wind contaminates the He lines, making the He I/He II ratio unreliable. 
- So, we cannot use Helium to classify the hottest O-stars.

**The Solution (Roman-Lopes et al. 2024):** https://arxiv.org/pdf/2609.25464
- Roman-Lopes (2024) shows how to classify these hot O2 stars.
- Instead of Helium, they use **Nitrogen lines** (specifically the **N IV / N III ratio**).
- **Why it works:** Nitrogen lines remain sensitive to temperature even when Helium lines are ruined by stellar winds. 
- N V lines are used as a secondary check.
- **For Luminosity:** They still try to use He II 4686, but they note it is "wind-sensitive" and hard to use at BOSS resolution.

**Summary of the Theory:**
- **Cooler O-stars (O4-O9.7):** Use He I / He II ratio (Martins 2018).
- **Hotter O-stars (O2-O3):** Helium fails due to stellar winds. You MUST use the N IV / N III ratio instead (Roman-Lopes 2024).
- **Terminology:** Spectral types are "morphological labels" (they look like a standard star). Temperature ranges (45-55 kK) are just "nuisance ranges" for scaling, not exact physical measurements.
- even though Martins 2018 doesnt use SDSS it uses archeive that has S/N ratio of  100 to 300 rather than that of SDSS S/N of  around 18 this methodolgy informs the approach but it hasnt been tested

-----------------------------------------------------------------------------------------------------------------------------------------------------------------
## Finding Photometric Error and Interstellar Reddening in SDSS FITS Files

To extract the required data, we first created a Python script named `Ar_e_r_Extraction.py`. Within the standard SDSS `.fits` files, the direct photometric error is not provided in the `HDU[2]` metadata table.
Instead, the pipeline stores the uncertainty as Inverse Variance (`SPECTROFLUX_IVAR`). We mathematically calculate the exact photometric error from this array using the formula $\text{Error} = 1 / \sqrt{\text{IVAR}}$. Furthermore, 
because physical interstellar reddening ($E(B-V)$) is entirely absent from these specific spectroscopic files,


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
--------------------------------------------------------------------------------------------------------------------------
#### 10/15/26

## Trust Region Reflective Alghorithm:

TRR (Trust Region Reflective) is a step-by-step optimization algorithm used to find the best parameters that minimize an error. It is especially useful when those parameters have allowed limits, like a temperature that must stay between certain values.

## How it works

1. **Start at an initial guess.**  
   The algorithm begins with some set of parameters.

2. **Build a simple local model.**  
   Around that guess, it makes a simplified mathematical picture of how the error changes nearby.

3. **Choose a trust region.**  
   It draws a small neighborhood around the current point. Inside this neighborhood, it trusts the simple model to be reasonably accurate.

4. **Solve the trust-region subproblem.**  
   It asks: “Within this small neighborhood, what step gives the best improvement according to the simple model?”

5. **Propose a new point.**  
   That best step gives a candidate new set of parameters.

6. **Handle bounds reflectively.**  
   If the step would go outside the allowed limits, the algorithm reflects it off the boundary instead of just cutting it off. This lets it slide along the edge and still move toward a good answer.

7. **Test the new point.**  
   It calculates the real error at the proposed new point.

8. **Compare actual vs. predicted improvement.**
   - If the real error improved about as much as the model predicted, the step is **accepted**, and the trust region may be **expanded**.
   - If the real error did not improve as predicted, the step is **rejected**, and the trust region is **shrunk**.

9. **Repeat.**  
   It keeps doing this loop: build model, choose region, solve subproblem, test, accept or reject, adjust region size.

10. **Stop when done.**  
    It stops when the step becomes very small, the error is low enough, or another stopping condition is met.

## The main weakness

Because TRR only looks at the nearby neighborhood, it can get stuck in a **local minimum** — a spot that looks good locally but is not the best overall answer.
