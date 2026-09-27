# Literature Review Log
**Logging about the papers I read and writing down the findings and drawbacks of each.**






## What I did:

**15th Sept 2026** 

**Read arXiv:1802.01724** (NIR classification)
https://arxiv.org/pdf/1802.01724
- Used NIR spectra to classify stars instead of opitcal spectra.
- Used only 92 Stars data from APOGEE and was only applied on 4 stars.
- for benchmarking 4 spectral lines (Br11, Br13, and two He II ) were used.
- used simple linear relations for line strength instead of machine learning.
- -----------
**Drawbacks**
- Was only applied on 4 stars which proves that this method is unstable to used as a benchmark. 
- In NIR spectra, very few spectral lines are available that can be appropiate for this method.

---------
**17th Sept 2026**

**Read Kyris et al (2022, A&A 657)**
https://www.aanda.org/articles/aa/full_html/2022/01/aa40224-20/aa40224-20.html
- Uses Machine learning to automate classification of OB stars. 
- Data obtained from GOSS, LAMOST.
- Only the spectra with S/N ratio > 50 were used rest were discarded.
- 4 RF models were used for accurate results.
- Only 70% accuracy was obtained due to physical limitations, the EW's were overlapping.
- This method proved better for O type  than early B type.
- ---------
**Drawbacks**
- The bottleneck is physical and cannot be resolved using machine learning or any method.
- The data obtained was taken from 4 different surveys i,e was heterogeneous.
- Requires high quality data (data with S/N > 50).
- Not applicable on all OB stars, isn't valid for early B type comparatively.
------------

**19th Sept 2026 , 14:18 hours**

**Read arXiv:2003.09469v1 (classification using NIR spectrum)**
https://arxiv.org/pdf/2003.09469v1
- 316 B-Star data obtained from APOGEE H-Band and LAMOST optical spectra. 
- For benchmarking, He I , Si II/V, Mg II and Balmer lines were used.
- measured EW and FWHM of Br11, Br13
- Used comparison between spectral lines obtained from optical and NIR spectra. 
- NIR provides additional information to distinguish late B and early A type stars.
---------
**Drawbacks**
- B3-A0 type stars give satisfactory results while B0-B2 stars deviate from it. (same as in other NIR papers)
- Classification relies on brackett lines which aren't that visible in NIR as compared to optical.
- Br13 dispersion near 16105A also lead to confusion.
- calibration of optical spectra with time to compare with NIR lead to data errors.
------------
**Read arXiv:2609.18590** (OB stars, tree-based ML)
https://arxiv.org/pdf/2609.18590
- Hand-measured equivalent widths were not used, but full normalized optical spectra (12,199 flux values) were used.
- Data: 1,535 OB stars and 80 A supergiants from IACOB (S/N > 50) taken from SIMBAD.
Compared 6 tree-based models: DT, RF, Extra Trees, XGBoost, LightGBM and HistGradientBoosting.
- 3 experiments: O/B/A (LightGBM ~98%), 6 bins of the spectral type (RF ~89%), spectral type + luminosity class (XGBoost ~77%).
- Showed that the models are based on real diagnostic lines: SHAP – used for O stars (He II), early B (Si III/O II/C III).
- -----------
**Drawbacks**
Simbad labels are noisy (particularly for B stars) so accuracy is only a measure of consistency with Simbad.
Tested only on a single uniform dataset (high resolution IACOB data downsampled to R = 4000); not tested on other instruments or other noisier survey data.
The Be-star problem is not mentioned, as Be/Oe stars, Of?p stars and binary stars were excluded.
- No error bars and just 6 coarse bins and one split.
The problem of accuracy is not with the algorithm, but is actually a problem with the MK scheme itself.

**Read Zenodo 13683948** (SDSS star classification, Random Forest)
https://zenodo.org/records/13683948
- Provides the classification of the main spectral classes A, F, G, K and carbon (C) stars from SDSS DR17.
- Inputs: u, g, r, i, z band values + Teff, log g, redshift, pseudocolor, variance.
- Imbalanced data using one Random Forest (100 trees) and compared 3 methods of imbalanced data: Original data, undersampling and SMOTE oversampling.
- Applied to two test sets: fixed (real data only) and stratified (can include synthetic data).
Accuracy for the stratified set: 0.87 original, 0.86 undersampled, 0.94 oversampled.
- -----------
**Drawbacks**
- The 0.94 is inflated: Test set has synthetic SMOTE samples. This is remarkably low considering that the real-data fixed set has the value of ~0.59.
Too few number of "O" stars, "B" stars are not classified.
The “C” class consists of carbon stars, carbon white dwarfs and CVs, which is not a single class.
Broad-band (not line-level) spectral class information. Teff already has much of the spectral class information encoded.
- No algorithm, no feature-important analysis, no error bars.
- The benchmark comparison contains various tasks and datasets (e.g. a 0.97 result is a binary A vs F).