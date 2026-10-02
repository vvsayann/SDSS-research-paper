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
## Reason
**Brackett line FWHM working better in cooler stars**
The reason that FWHM (full width at half maximum is the flux between continuum and line minimum) works better with cooler stars
is due to the ionization state of hydrogen which changes with the surrounding conditions such as pressure, for example a supergiant star 
will have larger radius but lower surface gravity compared to a dwarf star so the pressure is lower. Brackett line become broader with pressure
so thats why with stars that are cooler are narrower FWHM.