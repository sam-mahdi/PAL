# Anchor_Point_Finder *Program in beta, some features may not always work in all scenarios. 
This program searches through your peaklists and finds strips that contain both i and i-1 CA and CB peaks. 

These are good anchor points to start when trying to create your sequence chain for assignments. 

***PROGRAM ASSUMES AMIDE BACKBONE CHEMICAL SHIFT IN 2D IS IDENTICAL TO THE AMIDE VALUE IN THE 3D. I.E. Peak at 123.345 in the NHSQC, the CA and CB amide values in the HNCA and HNCACB must be 123.345***


There are 2 options to run:

***Run Without Matches***

This program only requires the peaklist files. No Carbon tolerance needed. 

It will search through the peaklists and find strip plots that contain both i and i-1 CA and CB peaks. 

If the HNCACB has been modified so only CBs show up, make sure to check the CB Only Flag. 

The output will contain the amide chemical shift values of peaks that contain both. And will be titled:
***i_and_i_minus_1_matches_only.txt***
***This file will be in the same directory as your peaklists***

```
Amide values of peaks with both i and i-1 CA and CB values 
?-?-?: 120.564
D338N-H: 119.256
V339N-H: 118.545
```

***Run With Matches***

This runs the same as without matches, however it additionally will search the peaklists to find i+1 and i-1 matches for the amide peaks that contain both i and i-1 CA/CBs. 

The purpose of this is, in  many cases you may have both i and i-1 CA/CB pairs, but you won't be able to find any matches in the strip plots. Essentially making this a very poor anchor point. So this program filters the previous file (without matches) by pairs that contain i-1 or i+1 matches. 

The carbon tolerance will be used for searching the strip plot (generally 0.2-0.3). The bigger the value, the more matches you get. The less the value, the more accurate the matches. 

When using the CBCACONH and HCNACB, one could get multiple CB (2 from HNCACB, 1 from CBCACONH) values. The CB_Tolerance is used to remove the duplicate CB values. Again, the program only mathes those that only have 2 CA and 2 CBs, so this extra pair would remove the peak from matches. The bigger the CB_Tolerance, the higher the chance you'll remove other peaks that aren't duplicates. So keep in mind the CB_Tolerance could remove CB peaks that aren't duplicates (i.e. i and i-1 CBs that have similar chemical shifts would be removed). 

Now the program does not make any assumptions on which CA/CB peaks are i and which are i-1. Instead, it will search every combination. 

If you have 4 peaks:
CA: 55.5 and 62.2
CB: 32.2 28.8

The program will search the strip plot for 4 pairs:
55.5 and 32.2
55.5 and 28.8
62.2 and 32.2 
62.2 and 28.8

The output file will be a csv file. 
The first column will be the label, the 2nd column will be the value of the amide peak. The 3rd column will be which of the 4 pairs was searched (only pairs with matches will be displayed, so not every amide peak will have 4 pairs). The final column will contain the matches from the CA/CB pair that was used. 

```
Label   Amide peak CA    CB      Matches
Q251N-H	118.959	55.093	26.897	116.529 118.033 118.825
 	 	            55.093	38.235	121.087 118.197 120.492
 	 	            57.647	26.897	116.117 118.558 122.159 124.785 106.910
 	 	            57.647	38.235	116.117
```

The user can then go to the amide peak, determine which pairs are the i and which ones i-1. 
```
Label   Amide peak CA    CB      Matches
Q251N-H	118.959	55.093	26.897	116.529 118.033 118.825 (user determined this is i pair)
 	 	            57.647	38.235	116.117 (user determined this is i-1 pair)
```
Now that the user knows which ones the i CA/CB and which one is the i-1 CA/CB. They have a good anchor point, with a guaranteed i-1 match. And 3 i+1 matches that they can then pursue. This would be a good anchor point.
