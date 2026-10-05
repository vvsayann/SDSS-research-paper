# Literature Reviews

## Date: 9/30/26 (Wednesday)

### Massive stars in the SDSS-V survey: New O2 stars in the Large Magellanic Cloud
**Authors:** A. Roman-Lopes, et al. | **Year:** 2026 | **Source:** arXiv (2609.25464)

#### 1. Introduction
Accurate classification of massive O-type stars is critical for understanding stellar evolution, but categorizing the hottest O-type stars (classes O1 through O3) presents a significant challenge. The extreme radiation pressure in these massive stars drives strong stellar winds that heavily contaminate standard Helium absorption lines, rendering them unreliable for precise diagnostic measurements. This paper aims to establish a new classification framework that bypasses this Helium contamination.

#### 2. Methodology
The study utilizes the SDSS-V and BOSS databases. Rather than relying on Helium and Hydrogen lines, it uses Nitrogen lines via the equivalent width (EW) method. Specifically, it employs the weighted ratio $\log|\text{EW(N IV }\lambda4058) / \text{EW(N III }\lambda4640)|$, which yielded values of 0.64 ± 0.29, 0.48 ± 0.23, and 0.34 ± 0.44 for specific targets (WSI 778, MGSD LH 117-43A/140, and Sk −69 135). This targeted data-driven approach successfully isolates the hottest massive stars in the O1–O3 subclass.

#### 3. Key Contributions
This methodology provides the most robust observational alternative currently available for classifying the hottest O-type stars. Because Nitrogen spectral lines remain relatively stable and distinct even in the presence of massive stellar winds, measuring their equivalent widths successfully circumvents the severe contamination issues that disrupt Helium lines.

#### 4. Limitations
The primary drawback of this approach is its inability to physically identify the stellar spectral type and luminosity class from fundamental physics. Because physical derivation is impossible with this methodology, researchers are forced to rely on empirical labels and template matching to classify the stars, which lacks theoretical depth.

#### 5. Conclusion
While the reliance on empirical labels presents a physical modeling limitation, the shift to Nitrogen-based equivalent widths successfully resolves the severe wind contamination issue for O1-O3 stars. This framework provides a highly practical empirical foundation for categorizing the hottest end of the O-type spectrum.

---

## Date: 10/2/26 (Friday)

### An Empirical Template Library of Stellar Spectra for a Wide Range of Spectral Classes, Luminosity Classes, and Metallicities Using SDSS BOSS Spectra
**Authors:** Aurora Y. Kesseli, et al. | **Year:** 2017 | **Source:** arXiv (1702.06957)

#### 1. Introduction
A persistent challenge in stellar classification is the discrepancy between theoretical atmospheric models and the actual observed spectra of stars. To address this, this study aims to construct a comprehensive library of stellar spectra based entirely on observational data. The primary objective is to use this library to reliably classify stars across the full Morgan-Keenan (MK) classification system, including massive O-type stars, using strictly empirical template matching.

#### 2. Methodology
The researchers constructed their templates using optical spectra obtained from the Sloan Digital Sky Survey (SDSS). They employed empirical template matching to classify the observed stars according to the MK system. To ensure high-fidelity template generation, the team enforced strict data quality constraints: they required photometric errors to be $e < 0.1$ magnitudes and capped the r-band interstellar extinction at $A_r < 0.25$ magnitudes. This rigorous filtering process successfully eliminated artificial reddening that could skew the classification pipelines.

#### 3. Key Contributions
The major advantage of this approach is its reliance on purely empirical data rather than theoretical models. By matching observations directly against high-quality, reddening-corrected observed templates, the methodology yields highly realistic classification results that avoid the assumptions and physical inaccuracies often introduced by synthetic atmospheric models.

#### 4. Limitations
While effective for the broader MK system, the framework presents distinct limitations for massive star research. The template matching process fails to accurately distinguish between dwarf and giant luminosity classes for early O and B-type stars. This failure stems from two main factors:
*   **Instrument Resolution:** The SDSS BOSS spectrographs operate at a medium resolution ($R \approx 2000$). This resolution smears out the subtle differences in spectral line widths (Stark broadening) driven by surface gravity that normally distinguish dwarfs from giants.
*   **Sample Size Constraints:** O-type stars are incredibly rare, resulting in a critically small sample size. Lacking enough reference data to build separate, statistically significant templates for massive dwarfs and giants, the algorithm was forced to group them together.

Ultimately, these factors force the framework to merge luminosity classes for hot stars, severely reducing its diagnostic power for massive stellar evolution.

#### 5. Conclusion
While this purely empirical template library offers realistic spectral typing and rigorous data quality controls, its small sample size for O-type stars and its inability to resolve early-type luminosity classes limit its precision for detailed massive star studies. However, its strict empirical framework provides an excellent baseline for how data-driven template matching can be executed.