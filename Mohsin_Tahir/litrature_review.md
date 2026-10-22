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
### Results:
mportantly, the current model's quantitative results cap at an effective t
emperature of $25{,}000$ K (early B-type). Because the neural network was trained on synthetic grids generated
under the assumption of Local Thermodynamic Equilibrium (LTE), it cannot accurately classify true O-type stars
($T_{\text{eff}} > 25{,}000$ K). At these extreme temperatures, intense UV radiation fields and strong stellar
winds cause LTE approximations to completely break down. Therefore, future expansion of the pipeline to classify
O-type populations will require generating complex, 
computationally expensive non-LTE (NLTE) grids to account for this physics.

### Model availaiblity:
while the zeta pipeline is not present you can download the payne base model and train it yourself The Payne is open-source software released under the MIT License.
- link: https://github.com/pacargile/ThePayne
The code repository is publicly available on GitHub.
- link: GitHub: hutchresearch/ZetaPayne

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

### BOSS Net availability:
while the standalone BOSS Net pipeline is not present as a simple download, you can access its pre-computed stellar parameters directly through the public SDSS Data Releases. The broader SDSS pipeline codebase is open-source software hosted on GitHub.

- link: https://github.com/sdss
- The model and its trained weights are available as a standalone archived release on Zenodo (with weights up to v2.0.0 as of January 2025).
- link: Zenodo: hutchresearch/BOSSNet

### APOGEE Net availability:
while the official APOGEE Net pipeline is integrated directly into SDSS DR17 data processing, you can query the pre-calculated results for millions of stars from the public SDSS catalog. Additionally, the original APOGEENet neural network model by the authors is available as open-source software.

- link: https://github.com/dsprague/APOGEENet (Original Base Model)
 
- link: https://github.com/sdss (Official SDSS Pipeline & Catalogs)

The code repository is publicly available on GitHub.
- link: GitHub: hutchresearch/ApogeeNet2

----------------------------------------------------------------------------------------------------------------
#### 10/15/26(thursday)
### Stellar labels for hot stars from low-resolution spectra – I. the HotPayne method and results for 330, 000 stars from LAMOST DR6  https://arxiv.org/pdf/2108.02878

#### 1. Introductions:
n this paper, the authors develop the HotPayne model specifically to classify hot stars (OBA type), 
as it is very difficult to classify them rather than cool stars due to weak metallic lines 
and rapid rotation.   To solve this, synthetic spectra generated from the Kurucz software under 
Local Thermodynamic Equilibrium (LTE) assumptions are used to train the HotPayne model. 
Once trained, it is applied to LAMOST survey spectra to simultaneously classify 11 labels, 
such as $T_{\text{eff}}$, $\log g$, $v \sin i$, metallicity, and chemical compositions like Si and C. 
Ultimately,
this method allowed them to extract parameters for over 330,000 hot stars.

#### 2. Methodology:


##### 2.1 Synthetic Generation

To create the training data, the authors generated a library of 10,127 synthetic spectra from first principles using the Kurucz software (`ATLAS12` for atmospheric structure and `SYNTHE` for radiative transfer). These physical models were computed entirely under LTE assumptions. sine the spectra has ultra high resolving power R= 500,00 To make the theoretical models look like real LAMOST observations they degraded the resolution to match the exact Line Spread Function (LSF) of the LAMOST spectrographs.

##### 2.2 HotPayne Model Training


 The network uses 17 input parameters (the 11 physical stellar labels plus 6 polynomial coefficients describing the telescope's LSF). The data passes through two hidden layers, each containing exactly 100 neurons, using a Sigmoid activation function.

then it is Built in PyTorch and optimized using the ADAM algorithm, the network was trained on 9,115 Kurucz spectra and validated on a hidden set of 1,012 test spectra.

then The trained neural network performed exceptionally well, predicting the synthetic flux with an average error of just 0.165% across the spectrum, proving it successfully learned the Kurucz physics.

##### 2.3 Spectral Fitting and Masking

Once fully trained, the HotPayne model is applied to the real LAMOST DR6 spectra to find the best fit for all 11 labels simultaneously via $\chi^2$ minimization. During fitting, they masked out bad data like telluric bands and interstellar absorption.
A critical adjustment was required for early A-type stars ($T_{\text{eff}} \sim 9500\text{ K}$). At this temperature, Hydrogen lines reach their maximum strength, causing the spectral gradients to reverse. This tricked the model and created an artificial "desert" of stars in their graphs. To resolve this, they completely masked the Hydrogen lines when fitting early A-type stars.

## 3. Key Contributions

- It successfully extracts highly precise information from low-resolution optical spectra, allowing for the simultaneous fitting of 11 stellar labels.

- It represents the first massive-scale classification of hot stars, expanding the sample size by two orders of magnitude to over 330,000 OBA star.

- It proves that automated neural networks can accurately measure complex kinematic parameters like projected rotational velocity ($v \sin i$) and microturbulent velocity ($v_{\text{mic}}$) directly from heavily blended spectral features.

## 4. Limitations 

- The most significant limitation is its reliance on LTE assumptions. For very hot stars ($T_{\text{eff}} > 25,000\text{ K}$) , LTE physics completely breaks down due to intense UV radiation and stellar winds dictating the atomic states (NLTE effects).

- Because of this LTE failure, HotPayne suffers from severe systematic errors on hot stars: it underestimates $T_{\text{eff}}$ by up to $3,000\text{ K}$, overestimates surface gravity ($\log g$), and inflates Helium and microturbulence abundances to artificially compensate for deeper NLTE spectral lines.

- The model assumes single, static stars, meaning it struggles to accurately classify binary star systems or O/B stars that exhibit emission lines.

## Model availaibility:
there is no Hotpayne model availaible for public but we can recreate it ourself using the base Payne model wiht out own liking


--------------------------------------------------------------------------------------------------------
#### 10/22/26 (thursday)
### Spectra Recognition Model for O-type Stars Based on Data Augmentation https://doi.org/10.3389/fspas.2021.634328

#### 1. Introduction:

In this paper, the authors develop the LCGAN model to automatically identify rare O-type stars from the LAMOST 
telescope survey. Because O-type stars make up less than 1% of the survey compared to millions of 
cooler F, G, and K stars, standard neural networks fail to recognize them due to a lack of training
examples. To solve this scarcity problem, the authors use a generative network to create 10,000 synthetic 
O-type spectra from just 150 real O-type spectra. These synthetic O-type spectra are then combined with 
real F, G, and K star spectra to train a deep classification model that can accurately find real 
O-type stars in large surveys.

#### 2. Methodology:

##### 2.1 Data Preprocessing

The authors collect low-resolution spectra ($R \sim 1800$) covering wavelengths from 3,690 to 9,100 Angstroms
from the LAMOST dataset, including 323 real O-type stars and 10,000 stars each for F, G, and K types. 
Because stars are at different distances, their overall brightness varies wildly and can confuse the c
omputer. To fix this, the authors scale every spectrum so its brightness values sit between 0 and 1, 
ensuring the model only looks at spectral line shapes rather than raw brightness.

##### 2.2 Synthetic Data Generation with LCGAN

To fix the shortage of O-type stars, the authors train the LCGAN model on 150 real O-type spectra to generate 
10,000 synthetic O-type spectra. The model works as a  between a generator that draws fake spectra from 
random noise and a discriminator that tries to spot the fakes until the generated spectra look completely 
real. 


##### 2.3 O-type Star Classification Model

Once the 10,000 synthetic O-type spectra are generated, they are mixed with 10,000 real F, 10,000 real G, and 
10,000 real K spectra to create a balanced training set of 40,000 stars. This balanced dataset is used to 
train a classification network that learns to distinguish O-type stars from the cooler stars.
The classifier model that is based on RAC-net uses an attention mechanism that focuses on the 
specific wavelength bands containing key 
O-type star features while ignoring noisy atmospheric bands, alongside shortcut connections that keep the 
deep network stable during training.

## 3. Key Contributions

- It solves the extreme shortage of O-type stars in astronomical surveys by generating realistic synthetic 
spectra.

- It combines synthetic data augmentation with an attention-based classifier that automatically focuses on 
the most informative wavelength regions while filtering out background noise.

## 4. Limitations

- The generator just copies the overall shape of real spectra without 
understanding the actual astrophysics behind the absorption lines.

- If the generator is trained for too long, it can suffer from mode collapse, meaning it gets stuck producing 
the same few spectra repeatedly and causes the classification accuracy to fluctuate.

- The model only classifies a star generally as an O-type star against F, G, and K stars, rather than breaking
O-type stars down into finer subtypes or measuring physical 
parameters like temperature and luminosity.

## 5. Results

First, the authors tested the quality of the 10,000 synthetic O-type spectra against an older generative model
called SGAN. Their LCGAN model achieved a realism score (GAN-test) of 95.48%, beating SGAN by 12.35%, and a 
variety score (GAN-train) of 91.50%, proving that the synthetic spectra are both realistic and diverse.
Next, after training the final classifier on the 40,000 balanced spectra (synthetic O-type plus real F, G, and 
K stars), they tested it on 323 real O-type spectra from LAMOST. The classifier achieved a 93.67% recognition
accuracy on real O-type stars, which is 8.66% higher than training the same classifier without synthetic data
(85.1%) and 3.31% higher than using SGAN. However, the authors noted that training the generator 
beyond 1,200 iterations caused minor accuracy oscillations due to the generator occasionally repeating 
similar spectra.

## Model Availability:
Neither the LCGAN model nor the O-type Spectra Recognition Model is publicly available to download, and 
only the raw LAMOST DR7 and DR8 spectra are provided online. However, we can recreate both models ourselves 
in Python using 
Keras by following the layer diagrams and training parameters given in the paper.




#### 10/24/26 (saturday)
### A new automated tool for the spectral classification of OB stars https://doi.org/10.1051/0004-6361/202142491[cite: 13]

#### 1. Introduction:

In this paper, the authors develop an automated machine learning tool using the Random Forest algorithm to 
classify OB-type stars into 11 sub-types ranging from O2 to B9. Traditional visual classification is 
subjective and unable to keep pace with massive spectroscopic surveys like LAMOST, GOSSS, 2dF, and VFTS
.To solve this, the authors build a robust classifier based on equivalent width measurements of 
17 non-Balmer spectral lines that works independently of luminosity class and across varying metallicities
.

#### 2. Methodology:

##### 2.1 Spectroscopic Data and Quality Filtering

The authors compile a multi-survey training dataset containing 5,329 high-quality spectra from Galactic 
and Magellanic Cloud surveys (LAMOST, GOSSS, 2dF, VFTS) covering different metallicities. 
To ensure reliable line measurements, they filter out all spectra with a signal-to-noise ratio below 50 ($S/N > 50$). 
They also group 32 detailed spectral sub-types into 11 broad adaptive binned classes 
($\text{O2-O6}$ through $\text{B9}$) to ensure adequate training samples per class.

##### 2.2 Equivalent Width (EW) Feature Extraction

 the authors quantify line intensities by measuring the equivalent width (EW) of 17 characteristic 
 non-Balmer spectral lines—primarily Helium ($\text{He I}, \text{He II}$) and metal lines 
 ($\text{Mg II}, \text{Si III}$, etc.)—using Gaussian profile fitting. Non-detections or 
 failed fits are handled using designated constant to retain valuable diagnostic 
 information without discarding incomplete spectra.

##### 2.3 Machine Learning Classifiers and Augmentation

The core classification uses the supervised Random Forest (RF) algorithm, complemented by Probabilistic Random
Forest (PRF) to account for measurement errors and a novel KDE-RF method. The KDE-RF method applies 
Kernel Density Estimation to simulate 11,000 balanced mock training objects, smoothing sparsely sampled 
feature spaces and resolving class imbalance. Sequential feature selection confirms that all 17 
spectral lines are necessary to maximize classification performance across different sub-types.

## 3. Key Contributions

- It introduces a specialized automated classifier for OB stars that completely bypasses 
variable Hydrogen Balmer lines, avoiding false classifications caused by circumstellar disks.

- It successfully combines multi-survey data from different telescopes across multiple metallicities 
(Galaxy, LMC, SMC), making the model widely applicable to diverse galactic environments.

- It develops and evaluates three distinct Random Forest implementations—including 
the novel KDE-RF simulation method—proving that tree-based algorithms handle multi-class 
spectral classification reliably.

## 4. Limitations

- The model achieves an overall accuracy ceiling of ~70%, restricted by the intrinsic physical scatter of 
equivalent width distributions within adjacent spectral classes rather 
than measurement errors.

- The classifier performs broad sub-type bucket classification (11 classes) rather then finding steller
parameters

## 5. Results

When evaluated on a 30% test set (1,599 stars), the standard RF, PRF, and KDE-RF models all achieved a 
consistent overall accuracy score of ~70%, with cross-validation scores confirming high stability 
($69\text{--}70\%$). Performance metrics varied by sub-class: early O-stars ($\text{O2-O6}$)
and late B-stars ($\text{B9}$) achieved high recall scores ($>0.97$ and $0.67\text{--}0.72$ respectively), 
whereas intermediate classes like B1, B2, and B8 underperformed with F1-scores dropping to $0.42\text{--}0.61$ 
due to natural EW overlapping. Error analysis revealed that the vast majority of misclassified objects 
fell into immediately neighboring spectral classes, reflecting the continuous physical 
nature of stellar temperature. When applied to blind real-world test cases 
(328 stars from the high-resolution IACOB survey and BeXRB companion stars), 
the model correctly matched published classifications in 66% of cases and 
predicted adjacent classes for the remainder, proving its strong generalization 
capability on unseen observational data.

## Model Availability:

The pre-processed training datasets and the complete Python code implementing the Random Forest 
classifiers are publicly available on GitHub at `https://github.com/EliasKyritsis/SpectralClassifier.