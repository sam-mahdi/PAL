# Sams_Strip_Plot

Works similar to SPARKYs strip plot. 

Will search through the peaklists and output matches to user defined values. Additionally, can use BMRB average chemical shift ranges for amino acids to predict amino acid type using inputed chemical shift values. 

***THIS PROGRAM WORKS ON THE ASSUMPTION THE AMIDE BACKBONE NITROGEN AND HYDROGEN VALUES IN THE 2D DATA, ARE IDENTICAL TO PEAKS PICKED IN THE 3D DATA. OTHERWISE THE PROGRAM WILL NOT WORK. IF "PEAK CENTER" HAS BEEN USED, THOSE VALUES WILL NOT BE THE SAME AND THIS PROGRAM WILL NOT WORK FOR THOSE PEAKS***

To use: 

***Short version***
Simply upload peaklist files. Input tolerances (usually 0.2 for carbon, 0.02 for hydrogen). Input chemical shift values, and check the boxes for the experiments you want to run. 
I.E. "CA Only" searches HNCA. "CA CB" searches HNCACB. To display the matches, make sure to checkbox "Display Carbon Matches" for 3D data searches, or the display NOE options for NOE filtered matches. 

To identify amino acid type. Simply input chemical shift values of your search, and click identify. If no matches are found, you will only get an output of your inputed chemical shifts. 

***Long Version***

Upload peaklist files you want to search through. Click the "Upload Peaklist Files" Button, and a window will pop up. 

Just use the browse button to upload your peaklist files (you don't need to upload NHSQC files to use the strip plot). 

Once you've loaded up the peaklists, simply exit the window. 

The Carbon and Hydrogen tolerance is the deviation the matches can have from the user inputed values. 
Carbon is generally 0.2, Hydrogen is 0.02. 

Then you may input your CA, CB, CO, and Nitrogen values. 

The CA, CB, and CO may be i or i-1 chemical shifts, depending on the direction you are searching (i-1, or i+1). 

The Nitrogen will ALWAYS be the value of the i peak (the one you are looking at). 

***Make sure to click enter for every value***

The check boxes will define what peaklists are searched. 

E.G. If you are going backwards, you would input the i-1 CA, CB, and CO values. 

The "CA Only" checkbox will search the HNCA peaklist file for matches. 

The "CA CB" will search the HNCA peaklist file for matches, then filter those matches with the CB value in the HNCACB

```
CA: 62.3
CB: 32.5
#CA only output
123.5
120.2
115.5
#CA CB output
120.2
```
In the above example, the HNCA had 3 matches, but only one of those had a CB at the value defined by the user. 

The order "left to right" indicates the search/filter order. 

The "CA CB CO" search the HNCA peaklist first, then the HNCACB, and finally the HNCACO. 

For going forward, its the same philosophy. 

The "CA CO" now searches the HNCA, then filters those matches using the HNCO. 

***CA only and CA CB is used for both directions, going forward and backwards***

The NOE section defines what NOE ranges it will look for matches. This filter the above 3D data searches. 

If "NH NOE" and "CA Only" is checked, the program will filter your CA matches using NOE matches. I.E. The i-1, i, and i+1 peak should have NOE crosspeaks to each other. This searches for those and filters matches using them. 

The same is true for HA. Thus, you may also search for cross peaks for regions where HA show up. 

The above checkboxes all run the program. However, they do not display the matches. 

To display the matches, you must check the display boxes. 

"Display Carbon Matches" will display matches from the 3D searches. 

"Display NH NOE Matches" will ONLY display matches that have passed the NOE filter. 

"Display combined NOEs" will display matches ONLY shared between the NH and HA matches. 

***For amino acid type***
This program can also use BMRB average chemical shift ranges to predict what type of amino acid you are searching. 

To do so, simply input your chemical shift values and click identify. 

NOTE: CA and CB values are quite specific to amino acids, however CO, N, and NH ranges can vary quite a bit protein to protein, and thus can provide erronous results. 

By default, the program will use all information inputed. However, for i-1 searches, you don't have nitrogen or hydrogen amide values. As such, there is an option to exclude nitrogens in the search. 

The prediction is determined by the range of of chemical shifts typically observed for an amino acid. You may increase or decrease this range by adjusting the identity tolerance (i.e. increasing or decreasing the possible matches). Input fraction values (i.e. for 80% use 0.8). 

***To replace or remove inputted values, you must clear the entry box and click enter again, otherwise the old value will be kept and used in the search***


There is a conversion tool as well, but it only moves assigned peaks. To use, simply upload the peaklists and click convert. 

What this tool does is shift all the Nitrogen and Hydrogen values in 3D data, to an NHSQC peaklist. It will also move NOE peaks picked (these don't need to be assigned), using the old NHSQC peaklist, and the new one (again, this assumes no "peak center" has been used, and the NHSQC value of the amide backbone is identical to the one in the 3D data). You may of course transfer unassigned peaks, but their values will not be shifted. They will just be copy/pasted over with the same values in the new peaklist. You may also choose to only transfer CBs (if you have CB optimized experiments). 
