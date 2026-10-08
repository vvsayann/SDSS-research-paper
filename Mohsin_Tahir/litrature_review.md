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



-----------------------------------------------------------------------------------------------------------------

## Date: 10/2/26 (Friday)

### An Empirical Template Library of Stellar Spectra for a Wide Range of Spectral Classes, Luminosity Classes, and Metallicities Using SDSS BOSS Spectra
**Authors:** Aurora Y. Keslie, et al. | **Year:** 2017 | **Source:** arXiv (1702.06957)

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



--------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Date 10/7/26 (Wednesday)
### ZETA-PAYNE: a fully automated spectrum analysis algorithm for the Milky Way Mapper program of the SDSS-V survey : https://arxiv.org/pdf/2203.14538

### 1. Introduction
While the ZETA-PAYNE algorithm was developed as a generalized classification model for all early-type (O, B, A, and F) stars, its computational framework provides a robust foundation for strictly isolating and analyzing O-type populations. 
A critical advantage of this study is its empirical validation of optical spectroscopy over near-infrared (NIR) data for hot stars. Analysis demonstrates that utilizing SDSS optical data via the BOSS instrument yields substantially lower internal uncertainties compared to the APOGEE NIR spectra. 
Most notably, the error margin for effective temperature ($T_{\text{eff}}$) is restricted to just 1-2% in the optical regime, compared to 3-10% in the NIR. Similar accuracy improvements are observed across rotational velocity ($v \sin i$) and surface gravity ($\log g$) measurements.
Because O-type stars emit the vast majority of their flux in the ultraviolet and blue optical wavelengths,
prioritizing SDSS optical spectra is essential to minimize classification error and ensure highly precise stellar parameterization.

### 2. Methodology:
##### 2.1 The Model spectra:
First, the neural network generates the pure synthetic spectrum. The final "model spectrum" is then dynamically constructed by the ZETA-PAYNE minimizer so that it can be compared directly to the raw SDSS BOSS optical spectrum. After the initial SDSS reduction pipeline removes atmospheric interference (telluric contributions), the algorithm constructs the model using the general formula:

$$ \text{Flux} = \text{LSF} * \left[ \prod_i \text{Line}_i(T_{\text{eff}}, \log g, \dots) \right] \times \text{Response}(\lambda) $$

Here, the central term $\prod_i \text{Line}_i$ represents the pure spectral lines formed in the stellar photosphere, generated by the neural network. LSF is the line-spread function, which represents the physical blurring of the telescope optics. $\times \text{Response}(\lambda)$: This is a multiplicative factor applied across the different wavelengths ($\lambda$) to account for large-scale distortions, such as interstellar reddening and the camera sensor being more sensitive to red light than blue light. It is represented by:

$$ \text{Response}(\lambda) = \sum_i c_i T_i(\lambda) $$

#### 2.2 Neural Network configuration, training, and validation:
First, a sparsely pre-computed grid of synthetic models is generated, which the neural network interpolates efficiently. The neural network is then trained on a quasi-random grid which makes the coverage even for the whole grid, but here the authors found that there was some inferior performance in the APOGEE wavelength range in the regime of slowly rotating late A- to F-type stars ($T_{\text{eff}} \le 10{,}000$ K and $v \sin i \le 30$ km s$^{-1}$). The low performance of the neural network in this regime is associated with a high complexity of stellar spectra that are found to exhibit a large number of narrow spectral lines of metals as compared to the spectra of hotter and more rapidly rotating stars when trained on a quasi-random grid. For this solution, the authors added a random sample of models from a Gaussian distribution $T_{\text{eff}} \sim \mathcal{N}(6000, 3000)$, $v \sin i \sim \mathcal{N}(0, 25)$ which are main sequence stars. Now, a hybrid grid is made. The neural network is trained with the combined grid of 10,000 models, where 90 percent are used for training and the remaining 10 percent are used for validation. After the whole 10,000 iterations, the test set is used to check if the model is accurate. The actual learning and weight updates during this process are done using the RAdam optimizer, which acts as the mathematical engine.

#### 2.3 Model Fitting and Optimization

The ultimate goal of the ZETA-PAYNE algorithm is to find the exact stellar parameters (represented as the vector $\theta$) that make the generated model spectrum perfectly match the observed SDSS spectrum. To achieve this, the algorithm minimizes the $\chi^2$ merit function:

$$ \chi^2 = \sum_i \left( \frac{f_i - F(\theta, \lambda_i)}{\sigma_i} \right)^2 $$

Here, $f_i$ represents the raw observed flux from the telescope, $\sigma_i$ represents the observational error (noise) for that specific wavelength, and $F(\theta, \lambda_i)$ is the fully assembled model spectrum. 

As established earlier, this model spectrum relies on the neural network output ($\text{NN}$), the telescope blur ($\text{LSF}$), and the camera distortion ($R$). At this fitting stage, the algorithm also explicitly applies a Doppler shift operator ($D$) to account for the star's radial velocity ($v_r$), creating the final equation:

$$ F(\theta) = \{ \text{LSF} * D[\text{NN}(\theta, \lambda_i), v_r] \} \times R(\lambda_i) $$

To minimize the $\chi^2$ error, the system uses a mathematical technique called the "Trust Region Reflective" optimization algorithm. Initially, the authors tried starting this optimizer at the exact center of the training grid. However, they discovered a major problem: the algorithm would frequently get trapped in a "local minimum." This means the optimizer would find a mathematical valley that looked like the right answer locally, causing it to halt and output the wrong parameters by getting stuck just above or below a temperature of $10{,}000$ K.

To prevent the algorithm from getting stuck in the wrong temperature regime, ZETA-PAYNE employs another optimization process. Instead of starting blindly in the middle of the grid, the algorithm rapidly evaluates the $\chi^2$ error at numerous points across the entire stellar parameter space. The algorithm identifies which of those sample points produced the lowest $\chi^2$ error and selects it as the most accurate initial guess. The Trust Region Reflective algorithm then takes over from this optimized starting point, fine-tuning the stellar parameters and the response function until it perfectly dials in on the true global minimum.

#### Key contributions
- You can input raw un-normalized data directly into the ZETA-PAYNE model.
- Because the neural network is differentiable, it can use gradient descent to achieve high-precision results even if the original training data is discrete.
- Instead of calculating physical telescope blurring, interstellar space dust (reddening), and atmospheric interference as three separate steps, ZETA-PAYNE models them all simultaneously using the Line Spread Function (LSF) and the Response function.

#### Limitations:
- The neural network models only based on what it knows from its training grid; if there is an extreme high-temperature O-type star that falls outside its limits, it will not fit it correctly.
- There are massive upfront computational costs to generate the physical grid and train the neural network.


-------------------------------------------------------------------------------------------------------------------------------------------------------------
#### 10/7/26 - 10/8/26
### A self-consistent data-driven model for determining stellar parameters from optical and near-IR spectra:https://arxiv.org/pdf/2402.05184

#### 1. Introduction
In this paper, the authors use machine learning to infer physical stellar parameters 
directly from spectra, rather than classifying them using the traditional MK system. 
Specifically, the study develops BOSS Net—a data-driven pipeline for optical spectra—
as the counterpart to their updated near-IR model, APOGEE Net. By including a vast range of
stellar types, from brown dwarfs to white dwarfs, the models achieve comprehensive 
coverage across $1700 < T_{\text{eff}} < 100{,}000$ K and $0 < \log g < 10$. 
This wide range ensures that BOSS Net can reliably measure the parameters of most commonly 
observed objects within this space. 



### 2. Methodology

##### 2.1 Training Data (OBA Stars)
For this review, we focus exclusively on the methodology applied to hot, massive OBA-type
stars. To train the BOSS Net model, the authors utilized 128,430 LAMOST spectra and 
only 663 BOSS spectra. This heavy reliance on LAMOST data is due to the historical 
scarcity of high-mass OBA-type targets in legacy SDSS/BOSS surveys. 
By importing the massive LAMOST dataset, the authors provided the neural network with 
enough high S/N examples to properly learn the physical features of hot stars.

##### 2.2 Model Architecture
BOSS Net is a 1D residual convolutional neural network that takes the raw, un-normalized 
star spectrum as its direct input. To regularize the network and avoid overfitting, 
data augmentation techniques are employed during training. 
These techniques include dropping specific flux values, 
randomly removing continuous segments of the spectrum entirely, 
and adding artificial Gaussian noise based on the error margin. 
This forces the model to become highly robust at identifying true stellar properties, 
rather than strictly depending on or memorizing camera noise within the training dataset. 
After passing through multiple convolutional and fully connected layers, 
the network directly outputs the final stellar properties.

### 3. Results
The BOSS Net model demonstrates high reliability, though its precision is mathematically 
higher for cool stars than for hot (OBA-type) stars. The typical uncertainties for 
sources with a Signal-to-Noise Ratio (SNR) > 15 are summarized below:

| Stellar Parameter | Cool Stars ($T_{\text{eff}} < 6700$ K) | Hot Stars (OBA Type) | Unit |
| :--- | :--- | :--- | :--- |
| **Effective Temperature ($T_{\text{eff}}$)** | 0.007 | 0.02 | dex |
| **Surface Gravity ($\log g$)** | 0.09 | 0.13 | dex |
| **Metallicity ([Fe/H])** | 0.07 | 0.16 | dex |
| **Radial Velocity (RV)** | 7.0 | 12.5 | km/s |

### 4. Key Contributions
* **Direct Inference:** rather than using iteratively generate synthetic, computerized spectra to fit the data, BOSS Net takes a raw input spectrum and directly calculates the stellar outputs in a single forward pass.
* **Broad Scope:** The pipeline successfully maps a massive parameter space, applying a single data-driven model to a vast spectrum of star types.

### 5. Limitations
* **Lower Precision on Hot Stars:** BOSS Net is less accurate for hot stars compared to cool stars. Because hot OBA atmospheres lack the dense forests of molecular and neutral metal absorption lines found in cooler stars, the network has fewer anchor points to read. Consequently, the uncertainties in $T_{\text{eff}}$ and $\log g$ are significantly larger for hot stars.