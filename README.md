# PAL
This Library contains 4 different programs designed to assist in assigning NMR peaks using SPARKY. 

***AVS (Assignment Verification using Sparta+)***
This program can generate SPARTA+ files from PDB structures. 
It can also convert said generated SPARTA+ (or BMRB average chemical shifts) file into a format that can be used for APS. 
It can also check the all the SPARTA+ predictions (or BMRB average chemical shifts) against an NMRSTAR file, by calculating the RMSD of each assigned peak to its predicted values. 
It can convert SPARKY peaklists to NMRSTAR format, while simulatameously checking for incorrect assignments and improper labeling. 
Finally, it can run TALOS+ on the NMRSTAR files, and map out secondary structure predictions and S2 on a PDB file. 

***APS (Assignment Prediction using SPARTA+)***
This program calculates the RMSD of of experimental chemical shifts (provided via a text file), against the SPARTA+ predictions (provided by AVS). 
There are 2 different ways to calculate the RMSD within this program. 

***Strip Plot***
This functions similar to SPARKYs strip plot. It is entirely text based. 
Chemical shift information is put in for CA, CB, or CO, and is search through various experiments (HNCA, HNCACB, HNCACO, HNCO, NOE etc.)
Has the benefit of enabling the concomitant search of multiple spectra (instead of through just one like in SPARKY). 

***NOE Distance Calculator***
Calculates the distance between various atoms in your PDB file. Lets the user search for atoms within a user-defined distance from a user-defined atom. 
Incredibly useful for NOESYs. 
