# Sams_Strip_Plot

How to Use (for Gianluca):

Pretty self explanatory now. Add peaklist files for the experiments you ran. Again as before, peaks must all have the same nitrogen value (i.e. don't use peak center). 

Tolerance for carbon is 0.2, hydrogen 0.1 (but you can change these depending on how flexilble or stringent you want your strip plot to be). 

The CO for going backwards (i-1) is the HNCACO, using HNCO carbonyl peak. The CO for going foward is the HNCO, using the HNCACO carbonyl peak.

For NOEs, you can look at NH and HA range for comparisons. Check the box for the atoms to search (e.g. CA only checks the HNCA only, CA, CB checks HNCA and HNCACB, CA, CB, CO checks HNCA, HNCACB, and HNCACO, etc.). 

To display, simply check the display box. Carbon shows the strip plot for the 3D strip plot. The NH, HA NOE display shows the printout from the NOEs. 

To use: Simply type in the values of your atoms. 
e.g. if you want to find the i+1, type in the nitrogen of your i, the i CA, i CB, and i CO. The printout will be of other peaks (only displaying nitrogen value) that share the CA, CB, and CO values you inputted. 

Since I don't have HNCACO data like you do, I haven't been able to test that out. So let me know if that part works properly or not. 

**I've added a new conversion tool (you'll find it where you upload your peaklist files). If you used "pc" when peak picking, use this tool first (only works on assigned peaks)** 

This will replace the nitrogen value of your 3D data of ONLY YOUR ASSIGNED PEAKS, with the value in your NHSQC. 

So lets say you used "pc" for a peak in either your 2D or 3D, and thus the nitrogen value in the 3D doesn't match what you have in your NHSQC. This tool will change the 3D value so it matches the 2D. A new peaklist will be written containing these new values. If you wish to carry over your unassigned data, just make sure you check the box. No changes will be made to those peaks. 

You may also carry over the NOEs of your assigned peaks, but to do so you have to upload the a peaklist of the NHSQC before you moved the 2D peaks around (this is more useful if you are transferring assignment, if you're just trying to get all your assigned peaks 3D data centered, ignore this). 

**This tool is exceptionally helpful when transferring assignments for 3D work. Often times, the majority of carbon values do not change in titrations or the addition of new domains. The amide backbone atoms will however. The logic is the same as above. Move your peaks in the NHSQC (recenter), then use that new peaklist with the old 3D data. The old 3D data's nitrogen and hydrogen values will now the same as your new peaklist. Only assigned peaks will be moved, and unless the "transfer unassigned peaks" is checked, the new peaklist will only contain the assigned peaks. You may also move all the NOE peaks as well, simply upload your old NOE peaklist, with the old NHSQC peaklist (prior to centering and moving your peaks). This will avoid having to repick all the shifted peaks in your 3D spectra. Make sure to go through your peaklists to recenter your carbon values (some items may have shifted in flight).**
