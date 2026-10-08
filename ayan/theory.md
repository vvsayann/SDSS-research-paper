# Theory finding Log
**Logs containing any information I understand myself by reading papers etc in my own words**

28-09-26 T22:26   
**Flags & Labels**

Flags basically tell us if a condition is true or false for example if any pixel in our data is good or bad,
they basically come under the bitmask package and from the name 'bitmask' they assign bit values which are 'True' or 'False'.
for example, in our file we have Zwarning flag which if 0 that means has no warnings, basically Zwarning tells us about the redshift
and in case of our data we have no redshift i,e Zwarning is 0, along with that we have other flags such as platequality or specprimary 
which describes the quality of our fit file.

Where as, Labels is tag which explains what something is or what it means, for example Star type or name of a spectral line etc.
for example, a class would be 'Star' and subclass would be 'OB' which describes the type of star, the label Sourcetype and target type
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

-----------
02-10-26 T18:44
<a id="reason"></a>
## FWHM
**Brackett line FWHM working better in cooler stars**  
The reason that FWHM (full width at half maximum is the flux between continuum and line minimum) works better with cooler stars
is due to the ionization state of hydrogen which changes with the surrounding conditions such as pressure, for example a supergiant star 
will have larger radius but lower surface gravity compared to a dwarf star so the pressure is lower. Brackett line become broader with pressure
so thats why with stars that are cooler are narrower FWHM.

--------------
02-10-26 T19:51 
## Gaia Distance 
Gaia was an astrometric mission designed to make an accurate 3D map of the milky way,
It calculates the red shift of the star and, then we can calculate the distance of the star using the red shift,
it was used so that the luminosity classification was making physical sense with the distance.

---------------

02-10-26 T20:48
## Luminosity Criteria  
**FOR arXiv:2407.04163**  
The main criteria for luminosity the paper (2407.04163) is the width of wings of H balmer absorption lines especially H-Alpha. Keeping the spectral 
subtype same, main sequence stars have a higher surface gravity and broader wings, where as giants and supergiants have comparatively low surface gravity
and the wings are narrower as well. The authors assign the class by comparing these profiles for standard stars. This criterion works best for B2 or later type as 
for earlier stars the wings become less sensitive to luminosity so they used silicon to helium lines for these types (Si III @ ~ 4553 A & He I @ ~ 4387 A), they generally increase
with luminosity. Near B0 subtype He II absorption is also useful.

**FOR arXiv:2003.09469v1**  
In this paper, they determined the luminosity class from optical spectra using H-Gamma and H-Alpha along with prominent N ,  Si, He features to distinguish giants 
and supergiants from main sequence stars. Then they used IR criterion using Br11 and Br13 Hydrogen line, they compared the EW(measures absorption strength) with their FWHM(measures line width). 
For later B stars giants and supergiants have narrower brackett lines as compared to that of main sequence stars. For earlier B stars ~ till B3, the lines overlap making the 
criterion unreliable for them. 

---------------



02-10-26 T21:47
## Stellar winds
Stellar winds are the streams of gas flowing outwards from the surface of the star into the space.  
**How it affects our classification method:**  For very bright B type supergiants, these winds are very strong. Since the paper's
method tries to estime the luminosity class using width and shape of balmer line as they depend on the star's surface gravity,
but in case of very luminous supergiants, strong interstellar winds can also change the Balmer line profile so the line shape also depends
on interstellar winds along with surface, 
-----------

03-10-26 T22:15
## Metal lines
I've noticed that B type stars in NIR mostly have abuandance of metal lines while He I and He II are still present in some amount, however this is not
the case for O type stars, they only have He and Si lines for the most part. 
------------

04-10-26 T 22:40  
## Br11
Dwarfs show broader Br11 profiles mainly because they have high surface gravity, which produces a denser pressure gas in the atmosphere where the line forms,
Nearby electrons and ions create electric fields that disturb hydrogen’s energy levels. This spreads the absorption over a wider range of wavelengths,
producing broad wings around Br11.

----------

06-10-26 T17:12
## Spitzer and hershel telsecope

**Spitzer**  
Launched in 2003 by NASA for Infrared observations to observe objects hidden by gas and dust clouds. It had an 85 cm mirror and in the start could observe
between 3-180 micrometer wavelength. The instrument had a cool down feature that would keep them cool so their own heat won't interfere with the incoming IR 
signals. Spitzer was used to study young stars, dusty planetary systems, exoplanets and distant galaxies. The biggest discovery made by spitzer was finding a ring
of saturn with diameter 300 times than that of the planet. Some other key discoveries are TRAPPIST-1 which discovered seven earth like planets. Its IR observations
can reveal real dust emissions around an OB star which we can compare if the OB star lies near a star forming region or near a dust structure. 



**Hershel**   
Hershel was an ESA mission launched in 2009 which ended in 2013 after it ran out of the Helium coolant system which was used to keep the instruments cool. It had a
3.5 metre mirror and could observe between 55-670 micrometer which is better and accurate than Spitzer. It discovered some gas and dust filaments in molecular clouds which
were a birthplace for stellar structure. For our OB star analysis, the data can help us determine a relationship how massive stars interact with their birthclouds like how earlier stars
lie near warmer dust.

---------

07-10-26 T22:30  
## Galactic Latitude  
Galactic latitude (b) is the distance of a star or any object above or below the plane of the milky way galaxy when the sun is our reference point. 
Milky way is roughly shaped like a disk and the Galactic latitude how far the object is from the disk's central plane.
b = 0° : object is in the direction of the galactic plane.
b = +20° : object is above the plane.
b = -20° : object is below the plane.
b = ±90° : object is in the direction of galactic pole.

When we used the condition < 20° we are taking the stars that are either above or below the plane , basically focus on the region only where O and B type stars are commonly found, they do have 
bigger number but other stars such as A, F, G are also present but in small numbers. 

-------------



