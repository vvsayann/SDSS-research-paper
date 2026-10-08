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
**Read arXiv:2003.09469v1** (classification using NIR spectrum)
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

The B star classification system had not been changed for a long time, older benchmarking criteria was not capable to distinguish
between subtypes having high S/N and the existing benchmarking standards had some inconsistencies as well, authors wanted to make a new
classification benchmarking / grid system, 

| Spectral Line     | Purpose                      |
|-------------------|------------------------------|
| Balmer line       | Luminosity / surface gravity | 
| Si/He I ratios    | Early B stars B0-B2          | 
| He I/Mg II ratios | Temperature classification   | 

They took HERMES high resolution spectra (R ~ 85000) which also had binary star system and Be stars as well which were later on removed to
solely focus on B star classification and developing a grid / benchmarking system for it, only 157 stars remainded for this and the resolution was
changed to ~ 4000, using the balmer line they introduced a luminosity criterion based on the balmer lines which was calibrated using 
α Persei (a star in the constellation Perseus), IC 4665 (Summer beehive cluster in constellation Ophiuchus) and Pleiades with 
Gaia distances, see [Gaia](./theory.md#gaia-distance-)  
and for the stars earlier than B2 Si /He I line were used because balmer lines are easily influenced due to gravity so with change in graivty
they will use their reliability as well, 

**Key-results:** The authors made a new list of 158 B type star, this new benchmark method matches the star's surface gravity
and true brightness which wasn't the case in the older methods. They also found that some very detailed types and separating some types
like B6 and B7 isn't very useful at this resolution. One very important thing in the paper was that the star's rotation also changes the 
He I / Mg II line ratio so older methods might work well for some stars.

**Drawbacks:** Some classes such as II, IV don't have good standard stars so they are harder to classify properly, This method also does not work
that accurately for stars earlier than B2 and for very bright supergiants because their stellar winds can affect the spectral lines.
This method is mainly designed for stars which have abuandace of metal lines similar to that of our sun which are at higher temperature so this might
not be reliable as temperature varies a lot. check [Stellar](./theory.md#Stellar-winds)  
Finally this method has to be done with careful / picked parameters such as the spectra picked, on top of that it has to be done manually by experts,
it is not a computer based automation yet so it takes a long amount of time and can have a far greater possible error %.



---------------------

28-09-26 T18:20  
**Read arXiv:2003.09469v1**  
https://arxiv.org/pdf/2003.09469  
Authors took 316 candidate B type stars manually selected in H Band from APOGEE (R ~ 22,500) and took optical spectra from LAMOST
(R~1800) to form a sample between optical and NIR spectra. Then they used MK (used when we need to find both the temperature and
the luminiosity of the star) style criteria [luminosity-criteria](./theory.md#luminosity-criteria), they used the following line ratios for benchmarking / template matching:

| Spectral Line             | Purpose                   |
|---------------------------|---------------------------|
| Si III/Si IV              | For early stars B0-B2/B3  | 
| He I/Mg II and He I/Si II | For mid types B3-B5       | 
| Balmer line and N II/He I | For luminosity indicators | 

Then they measured the EW and FWHM of Br11 and Br13 line using gaussian profile. They used these EW results and developed a linear
relationship with Br11+Br13 using jackknife resampling (You basically perform automation -> you run your classification but by 
each iteration you remove one thing till you run out.) which was restricted to B3-A0 stars for better results and accuracy.

**Key-results:** Br11 and Br13 increase linearly toward later spectral type (which is consistent with early O and early B type) however
Br13 gets scattered due to being blended as wavelength increases to ~16000 A. The fitted relation(which was earlier obtained with the help of
gaussian fitting)   
**SpType = 0.503 * EW[Br11 + Br13]** classifies B3-A0 stars within one spectral subtype.
FWHM of brackett lines work better at cooler stars compared to hot stars. See the [reason](./theory.md#fwhm)  
As the temperature increases, more metal lines appear but, they cannot be used as standard benchmark. 

**Drawbacks:** This calibration works well for only A0-B3 stars (the FWHM broadening being the main reason) along with this
method can be dominated by stars since luminosity is playing an important role in NIR and the seperation between the luminosity
and temperature isn't well established as well, As mentioned early Br13 was being blended but this issue was only flagged but not removed
at all, The spectrums were picked exclusively knowing the emission lines so it cannot be used as a generic methods for other random
spectras as well. 

----------------

03-10-26 T22:03  
**Read arXiv:2607.15409**  
https://arxiv.org/pdf/2607.15409  
B type stars have a very short amount of time in pre-main-sequence (PMS) before they get a stable core hydrogen burning. Authors found
some stars around the orion nebula that were previously classified with luminosity class I-III, but they combined spectral classification to re-classify
these stars again and improve the data-set of early stars around Orin.

| Feature                                      | Purpose                                                  |
|----------------------------------------------|----------------------------------------------------------|
| Gaia DR3, 2MASS / WISE                       | Select candidiates and construct optical / infrared CMDs | 
| Br11 + Br13 EW's                             | Estimate infrared spectral types from B2 to A0           | 
| Si/ He line ratios                           | Classifiy B stars optically                              |
| Balmer line profiles and optical metal lines | Check luminosity class and evolved star labels           | 
| PARSEC evolutionary tracks                   | Estime age, mass of the star                             |  

Authors matched sources in Gaia, 2MASS within 1arc second searching a specific region around the Orion Nebula. Along with that the brightness and color cuts reduced
~ 49000 sources to 53 B/early A type candidates, Out of these 53 37 had infrared spectral, 27 had optical spectra and 48 had at least one kind of the spectra. They took 
infrared data from APOGEE, while optical was obtained from LAMOST and ESO observations of archives. For infrared classification they developed a linear relationship 
between spectral type and combined the strength of Br11 and Br13, using three benchmarking templates per subtype from A0 to B2. Meanwhile, the optical line ratios and direct
comparisons also worked out, They also examined the balmer lines and metal lines [metal-lines](./theory.md#metal-lines)  , for early B stars without optical spectra they used 
NIR and surface gravity measures to provide luminosity constraints.  
**Key-results:** Authors obtained spectral classifications for 48 stars and age/mass for all 53 they narrowed down, optical and infrared
classifications generally narrowed down to one spectral subtype, several stars which were previously classified in the subtype I-III showved different class such as V-like spectra
according to this method. Some stars whoed variable brackett profiles, emission, magnetic pecularities making them useful for a following classification method similar to this one.    
**Drawbacks:** This method is very unreliable and incomplete because stars needed detections in all three catalogues and had to pass color cuts manually, compared to another 
catalogue 16 similar early type stars were missing in this sample while this sample included 23 absent form the comparison catalogue.
The brackett linear relation becames unreliable to stars later than A0 and emission can disrupt it. 


----------------------

04-10-26 T22:33  

**Read Hanson_1998**  
https://iopscience.iop.org/article/10.1086/300556/pdf  
Early studies showed that hydrogen and helium lines in the H band change with the spectral type, but had too few standards to separate temperature effects from luminosity effects.
The authors investigated these luminosity affects and developed a compact H-band classification scheme for late O and B stars.

| Spectral feature                 | Purpose                                                                             |
|----------------------------------|-------------------------------------------------------------------------------------|
| Br11 hydrogen line               | Spectral-type information, its width also helps distinguish dwarfs from supergiants |
| He II                            | Indicates O-type atmospheres                                                        |
| He I                             | Helps classify OB stars, but depends on both temperature and luminosity             |
| Br11/He I equivalent-width ratio | Helps distinguish early/mid-B dwarfs from supergiants of similar spectral type      |

Authors studies 34 spectroscopic standards spanning late O to late B, concentrating on dwarfs and supergiants. Spectra were obtained in 1997 with Fspec at the multiple mirror telescope
and Bok telescope at ~ 2000. S/N was > 120, although some spectra were at ~ 100. The classification features fit within the small interval 1.66 to 1.7 um.
Atmospheric absorption was removed using A-dwarf standards. They measured EW, and examined line profiles. They compared these measurements with established optical spectral types
and luminosity classes. Their approach consisted first that whether the star was a dwarf or supergiant, then do He and Br11 strength detection.  
**Key-results:** At the same B spectral type, supergiants generally showed stronger He I and weaker Br11 than dwarfs, while dwarfs showed broader Br11 profiles, read  [Br11](./theory.md#br11). Therefore, these line
strengths cannot be used for temperature indication without keeping the surface gravity and luminosity in consideration. He II was only detection in O type star in this example, around O9.
They followed these set of instructions for classification of dwarfs  

| Observed absorption pattern       | Suggested classification |
|-----------------------------------|--------------------------|
| Br11, He I and He II all detected | Late O or earlier        |
| Br11, He I , no detected He II    | O9–B1                    |
| Br11 , with He I                  | B2–B3                    |
| Br11  , without detected He I     | Late B to early A        |

These are broad guides and they weren't limited to this, but they followed these roughly. The authors suggested a precision of ~ two to three spectral subclasses when luminosity is known.
The Br11/He I ratio is generally larger in early/mid B dwarfs than in supergiants of the same type.
They also recommended S/N > 100 , R ~ 2000 or higher and comparison standards observed similar resolutions.  
**Drawbacks:** The 34 star sample is too small to make this as a reliable benchmarking guide that can be used for any sample. Temperature and luminosity are independent
Br11 measurements are affected by the removal of hydrogen absorption lines from atmospheric correct and by locating the continuum in the lines, the authors advised against trusting Br11
EW to better than 0.3A. The narrow wavelength interval includes only Br11 from hydrogen brackett series, testing additional brackett lines requires wider coverage and the possible He II 
luminosity effect needs a larger star sample.

-------------------


07-10-2026 T22:10  
**Read arXiv:1902.07607**  
https://arxiv.org/pdf/1902.07607  
OB stars play an important rule for the studying of the milky way's structure, composition chemically and the stellar evolution but the catalogues prior to this method contained bright objects nearby 
the target stars. The catalogues were missing B stars, so the authors decided to develop a new catalogue using LAMOST DR5 and targetted the outer arms of the galaxy and tried testing that wheter MK class can 
assign spectral subtype and luminosity classes to these stars with accuracy or no. 

| Spectral line                                                              | Purpose                                                                                                                         |
|----------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------|
| Ca II K, **3933 Å**, versus Hγ, **4340 Å**                                 | Choose hot star candidates that have relatively low calcium and hydrogen absorption                                             |
| Mean equivalent width of 9 Fe index                                        | Remove cooler stars that have higher metal absorption                                                                           |
| He I, especially **4471 Å**                                                | Be able to identify B-star spectra from visual inspection                                                                       |
| He II **4200, 4541 and 4686 Å**                                            | Determine subtype and luminosity of O stars                                                                                     |
| He I **4471 Å** / Mg II **4481 Å**                                         | Be able to tell the difference between B spectral subtypes, and be able to discriminate between late B and early A contaminants |
| Si IV **4089 Å** and Si III **4552–4568–4575 Å**                           | Draw conclusions about early B stars and their luminosity                                                                       |
| Si II **4128–4130 Å**, C II **4267 Å**, N II **3995 Å**, and O II features | Other subtype and luminosity diagnostics                                                                                        |
| Balmer-line strengths and profiles                                         | Provide assistance with temperature and luminosity classification                                                               |
| N III **4634–4640–4642 Å**                                                 | Other information on O-star subtypes and luminosity.                                                                            |

LAMOST is a 4m telescope which is capable of observing ~ 4000 spectra per light exposure. Low resolution spectra cover 370-900nm with R ~ 1800 with main targets of r 9 to 18 magnitudes. DR5 consisted of around
8 million spectra. Authors used  S/N > 15 cap which left only 5 million spectra and repeated observations  i,e all of these do not belong to a different star, some could be of same.
Authors then pursued to measure the EW of the spectral lines further they used 9 iron (Fe) index rather than relying on just spectral lines
Their first criteria was 
1. EW(Ca II K) < 2.5 − EW(Hγ)/8
2. −4.5 ≤ EW(Hγ) ≤14 Å
This gave them around 160,000 candidate spectra which can be used for their process later on. They rejected the spectra which contained strong Fe absorption lines which resulted in spectra getting narrowed down to 
12200 approximately, These were inspected using H, He and metal features. Their spectra were checked manually by different people so error % could be shortened down. Spectra which did not have He features were exempted. 
For further detail classification, they chose 22,000 OB star spectra using MKCLASS. This automation compares spectra using MK standards and degraded the template from 1.8Å to 2.8Å resolution which was according to the LAMOST 
blue spectrum resolution. They tested this method using randomly selected spectra of around 5000 using a S/N > 15 and Galactic latitude < 20° [Galactic-Latitude](./theory.md#galactic-latitude-)cap. They double checked this with classification of 1000 OB spectra out of which 
646 had meaningful MKCLASS output rated good or better which was used as accuracy comparison for their own results.

**Key-results:** The catalogue contains:

| Stars           | Quantity                       | 
|-----------------|--------------------------------|
| Normal O stars  | 135 spectra of 91 stars        | 
| Normal B stars  | 21,658 spectra of 15,087 stars | 
| Hot subdwarfs   | 948 spectra of 727 stars       | 
| White dwarfs    | 160 spectra of 127 stars       | 

The catalogue has around 22,900 spectra of 16,000 stars, but it also has subdwarfs and white dwarfs. The normal OB stars consist of total ~ 15,000 stars out of which 91 are O stars and rest are B stars. 
This method intially classified about 89 (22%) of stars earlier than B7 but later on this dropped to 57 (16% ) for B8 and B9 as their luminosity is very close to that of early A type stars. For spectra of good quality, MKCLASS
gave results very close to manual classification.  
**Drawbacks:** Out of the 15,000 OB star spectra, around ~ 6500 (43%) got failed MKCLASS output and some classifications were wrong physically. This method applies to selected subset rather than being automated
for any type of spectra. The template cannot classify stars earlier than O9 with good accuracy due to abundance of metal lines, rotation, emission and the data quality (spectra) obtained along with weak spectral lines due to luminosity. 
low S/N, bad pixels, background subtraction and unusually strong He lines can also cause failures. The main drawback about this method that it requires too many manual inspections when picking spectra which can be slow as well as can cause error
compared to machine accuracy. Metal features which are sensitive due to luminosity are weak at LAMOST resolution making the classification uncertain. 

-----------------

08-10-2026 T16:15  
**Read arXiv:2110.10669**  
https://arxiv.org/pdf/2110.10669  
older B star classifcation standards had inconsistend labels and the reference stars that were used were unsuitable and with time the classifcation needed an upgrade. The authors revised the grid and updated the criteria 
for the classification in order to the modern spectra. A standard star is used as a reference star whose spectrum defines the whole classification process. A standard star should be a single star not binary as the combined spectrum
can cause misleading result in other star classification. 

| Spectral line           | Purpose                              |
|-------------------------|--------------------------------------|
| Balmer-line wing widths | Mid/late-B luminosity classification |
| Si III/Si IV ratios     | Early-B temperature classification   |
| Si/He ratios            | Early-B luminosity classification    |
| He I/Mg II ratios       | Later-B temperature classification   |

The authors obtained multiple spectra at R ~ 85,000 from HERMES, removed spectras that would cause problems later on such as the ones obtained from double-lined binaries and Be stars. They tok 157 reference stars. They dropped the resolution to 
~ 4000 and classified using comparison. They also used gaia distances [gaia-distance](./theory.md#gaia-distance-) to help making the grid. They obtained the temperature information using ratios between different silicon lines. Hydrogen lines to
obtain the surface pressure, broader lines mean greater pressure, By obtaining surface gravity they could easily distuingish between luminosity classes. Hence, temperature and surface gravity are considered together.  
**Key-results:** The new grid is more consistent, they authors found out that subtypes such as B6 and B7 were not needed at that resolution and they also demonstarated that stellar rotation influences spectral line measurements. Their big work is that
the grid is now more consistent to the actual physical characteristic of B-type stars especially surface gravity and luminosity which wasn't the case in the old grid system. However, this does not mean that this new grid system can find / calculate any
physical property of the star, it just means it gives consistent measurements of those properties.  
**Drawbacks:**  The revised grid has drastic improvement but it has some limitations:
1. Balmer wings are less effective when we want to determine the luminosity for hottest B type stars.
2. Stellar winds [stellar-winds](./theory.md#stellar-winds) mess up the spectra of bright supergiant. 
3. some luminosity classes are still difficult to distinguish as the difference gap between them is very small. 
4. Different chemical abundance's also affect the spectral line strength, for hotter B type stars they have more metal lines present. 
5. Constant rotation of the star broadens and blends the spectral lines together.

-----------------------

























