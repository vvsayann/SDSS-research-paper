# Literature Review Log
**Logging about the papers I read and writing down the findings and drawbacks of each and any theory work I read.
Mainly working on B type stars**






## What I did:

15-09-26    
**Read arXiv:1802.01724** (NIR classification)
https://arxiv.org/pdf/1802.01724
- Used NIR spectra to classify stars instead of opitcal spectra.
- Used only 92 Stars data from APOGEE and was only applied on 4 stars.
- for benchmarking 4 spectral lines (Br11, Br13, and two He II ) were used.
- used simple linear relations for line strength instead of machine learning.  

**Drawbacks**  
- Was only applied on 4 stars which proves that this method is unstable to used as a benchmark. 
- In NIR spectra, very few spectral lines are available that can be appropiate for this method.

---------
17-09-26 T22:00   
**Read Kyris et al (2022, A&A 657)**
https://www.aanda.org/articles/aa/full_html/2022/01/aa40224-20/aa40224-20.html
- Uses Machine learning to automate classification of OB stars. 
- Data obtained from GOSS, LAMOST.
- Only the spectra with S/N ratio > 50 were used rest were discarded.
- 4 RF models were used for accurate results.
- Only 70% accuracy was obtained due to physical limitations, the EW's were overlapping.
- This method proved better for O type  than early B type.  

**Drawbacks**
- The bottleneck is physical and cannot be resolved using machine learning or any method.
- The data obtained was taken from 4 different surveys i,e was heterogeneous.
- Requires high quality data (data with S/N > 50).
- Not applicable on all OB stars, isn't valid for early B type comparatively.
------------

19-09-26 T14:18    
**Read arXiv:2003.09469v1 (classification using NIR spectrum)**
https://arxiv.org/pdf/2003.09469v1
- 316 B-Star data obtained from APOGEE H-Band and LAMOST optical spectra. 
- For benchmarking, He I , Si II/V, Mg II and Balmer lines were used.
- measured EW and FWHM of Br11, Br13
- Used comparison between spectral lines obtained from optical and NIR spectra. 
- NIR provides additional information to distinguish late B and early A type stars.  

**Drawbacks**
- B3-A0 type stars give satisfactory results while B0-B2 stars deviate from it. (same as in other NIR papers)
- Classification relies on brackett lines which aren't that visible in NIR as compared to optical.
- Br13 dispersion near 16105A also lead to confusion.
- calibration of optical spectra with time to compare with NIR lead to data errors.
------------
19-09-26 T16:10  
**Read arXiv:2609.18590** (OB stars, tree-based ML)
https://arxiv.org/pdf/2609.18590
- Hand-measured equivalent widths were not used, but full normalized optical spectra (12,199 flux values) were used.
- Data: 1,535 OB stars and 80 A supergiants from IACOB (S/N > 50) taken from SIMBAD.
Compared 6 tree-based models: DT, RF, Extra Trees, XGBoost, LightGBM and HistGradientBoosting.
- 3 experiments: O/B/A (LightGBM ~98%), 6 bins of the spectral type (RF ~89%), spectral type + luminosity class (XGBoost ~77%).
- Showed that the models are based on real diagnostic lines: SHAP – used for O stars (He II), early B (Si III/O II/C III).  

**Drawbacks**  
Simbad labels are noisy (particularly for B stars) so accuracy is only a measure of consistency with Simbad. Tested only on a single uniform dataset (high resolution IACOB data downsampled to R = 4000); not tested on other instruments or other noisier survey data.
-The Be-star problem is not mentioned, as Be/Oe stars, Of?p stars and binary stars were excluded.
- No error bars and just 6 coarse bins and one split.
The problem of accuracy is not with the algorithm, but is actually a problem with the MK scheme itself.
----------
19-09-26 T22:43
**Read Zenodo 13683948** (SDSS star classification, Random Forest)
https://zenodo.org/records/13683948
- Provides the classification of the main spectral classes A, F, G, K and carbon (C) stars from SDSS DR17.
- Inputs: u, g, r, i, z band values + Teff, log g, redshift, pseudocolor, variance.
- Imbalanced data using one Random Forest (100 trees) and compared 3 methods of imbalanced data: Original data, undersampling and SMOTE oversampling.
- Applied to two test sets: fixed (real data only) and stratified (can include synthetic data).
Accuracy for the stratified set: 0.87 original, 0.86 undersampled, 0.94 oversampled.  

**Drawbacks**
- The 0.94 is inflated: Test set has synthetic SMOTE samples. This is remarkably low considering that the real-data fixed set has the value of ~0.59.
Too few number of "O" stars, "B" stars are not classified.
The “C” class consists of carbon stars, carbon white dwarfs and CVs, which is not a single class.
Broad-band (not line-level) spectral class information. Teff already has much of the spectral class information encoded.
- No algorithm, no feature-important analysis, no error bars.
- The benchmark comparison contains various tasks and datasets (e.g. a 0.97 result is a binary A vs F).

---------------

27-09-26 T17:30    
**Read arXiv:2407.04163** (NIR Classifcation of B type stars)
https://arxiv.org/pdf/2407.04163

Taking R = 85000, the authors removed the binaries and Be stars from the B stars,
while only the remaining 157 stars were classified as standard, the spectral was degraded
to R~4000. They then proposed a new luminosity criteria for stars later than B2
using the width of Balmer lines and used the traditional He I and Si lines for stars earlier than B2.
The limitation ares related to the luminosity of the stars, sensitivity of B stars and that the bigger stars 
have metal composition, and this method was non automated which took a longer amount of time.

---------------------

28-09-26 T18:20  
**Read arXiv:2003.09469v1**
https://arxiv.org/pdf/2003.09469

The authors chose a set of 316 B type stars from APOGEE H-Band spectra and took optical spectra from LAMOST,
they fit the Br11 and Br13 line, calculated the EW and FWHM using a gaussian profile, The linear relation between the
spectral type and Br11+Br13 EW which fits perfectly for B3-A0 type stars, however this process is only valid for A0-B3 
type stars and not generic however this is a stable method for early B type star classification, the reason for it being weak
is the weakness of the luminosity class due to blending of these lines with optical spectra / labels and has low resolution. 

----------------


28-09-26 T22:26   
**Flags & Labels**

Flags basically tell us if a condition is true or false for example if any pixel in our data is good or bad,
they basically come under the bitmask package and from the name 'bitmask' they assign bit values which are 'True' or 'False'.
for example, in our file we have Zwarning flag which if 0 that means has no warnings, basically Zwarning tells us about the redshift
and in case of our data we have no redshift i,e Zwarning is 0, along with that we have other flags such as platequality or specprimary 
which describes the quality of our fit file.

Where as, Labels is tag which explains what something is or what it means, for example Star type or name of a spectral line etc.
forexample, a class would be 'Star' and subclass would be 'OB' which describes the type of star, the label Sourcetype and target type
describe how we obtained the star data or how it was targeted.

-------------

29-09-26 T23:41  
**Index**  

The fits file contain different index value containing different details about the spectrum or the data available.

| Index value | Name of the index | Details present                                                                     |
|-------------|-------------------|-------------------------------------------------------------------------------------|
| 0           | Primary           | File name / header only                                                             |
| 1           | COADD             | Contains info like flux, loglam and ivar                                            |
| 2           | SPECOBJECT        | Contains metadata like class and subclass                                           |
| 3           | SPZLINE           | Contains the line information, either emission or absorption with flux redshift etc |

--------------

30-09-26 T00:20
**Method for B type stars**  
Normally Optical spectra was used for the classification of B type stars, it provides a wide range of 
spectral lines such as He I , He II , Si I , balmer lines etc. However, the saturation and relative strength of 
these lines change with their subclass / subtype which ranges from 0-9 (B0-B9). However, the optical spectra 
has a drawback too which is the main reason behind the less accurate results which is known as 'interstellar extinction'
basically meaning the gas and dust between the star and our measuring telescope which causes the light to scatter causing our
spectrum to not be perfect.

Whereas near-infrared spectra (NIR) specially the H band around the range of 1.5 to 1.8 um as NIR spectra is less affected
by the gas and dust present before the star. NIR has prominent brackett lines whose EW are realted to the subtype which makes NIR
spectra better for automated fitting however the main drawback is that we cannot rely only on brackett lines, it is the only 
common line found in NIR and cannot be used as standard benchmarking line.



