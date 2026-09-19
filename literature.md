# Literature Review Log






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
