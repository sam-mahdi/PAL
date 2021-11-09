import tkinter as tk
from tkinter import *
import os
import threading
import webbrowser

root = tk.Tk()
root.title('PAL')
root.geometry('1200x200')

main_pathway=os.getcwd()

def AVS_thread():
    os.system('python3 AVS.py')

def APS_thread():
    os.system('python3 APS.py')

def strip_plot_thread():
    os.system('python3 strip_plot_sm.py')

def NOE_thread():
    os.system('python3 NOE_GUI.py')
    
def anchor_point_thread():
    os.system('python3 anchor_point_GUI.py')

def run_AVS():
    pathway=main_pathway+'/Peaklist_Assignment_Library-PAL/V3/AVS'
    os.chdir(pathway)
    AVS_threading=threading.Thread(target=AVS_thread)
    AVS_threading.start()


def run_APS():
    pathway=main_pathway+'/Peaklist_Assignment_Library-PAL/V3/APS'
    os.chdir(pathway)
    APS_threading=threading.Thread(target=APS_thread)
    APS_threading.start()

def run_strip_plot():
    pathway=main_pathway+'/Sams_Strip_Plot'
    os.chdir(pathway)
    strip_plot_threading=threading.Thread(target=strip_plot_thread)
    strip_plot_threading.start()

def run_NOE_distance():
    pathway=main_pathway+r'/NOE_Distance_Calculator'
    os.chdir(pathway)
    run_NOE_thread=threading.Thread(target=NOE_thread)
    run_NOE_thread.start()
    
def run_anchor_point():
    pathway=main_pathway+r'/Anchor_Point_Finder'
    os.chdir(pathway)
    run_anchor_point_thread=threading.Thread(target=anchor_point_thread)
    run_anchor_point_thread.start()
    


def help_button():
    webbrowser.open('https://github.com/sam-mahdi/PAL')



tk.Label(root,text='This program runs AVS (Assignment Verification using Sparta+). Generates SPARTA+ files, converts SPARKY peaklist to NMRSTAR formats, run TALOS+, and convert SPARTA+ files for APS').grid(row=0,column=1)
tk.Label(root,text='This program runs APS (Assignment Prediction using Sparta+). Calculates the RMSD of experimental chemical shifts against SPARTA+ predictions').grid(row=1,column=1)
tk.Label(root,text='This strip plot functions similar to SPARKYs strip plot. It enables the concomitant searching of multiple spectra (HNCACB, HNCA, HNCO, NOEs, etc.)').grid(row=2,column=1)
tk.Label(root,text='This program calculates the distance between atoms within a PDB structure. Enabling the user to find what atoms are within a user-defined distance of a user-defined amino acids atoms').grid(row=3,column=1)
tk.Label(root,text='This Program finds amide peaks that contain both i and i-1 CA/CB peaks. It can then filter these peaks by those that contain i-1 and i+1 matches in a strip plot').grid(row=4,column=1)


tk.Button(root,text='AVS',command=run_AVS).grid(row=0,column=0)
tk.Button(root,text='APS',command=run_APS).grid(row=1,column=0)
tk.Button(root,text='Strip Plot',command=run_strip_plot).grid(row=2,column=0)
tk.Button(root,text='NOE Distance Calculator',command=run_NOE_distance).grid(row=3,column=0)
tk.Button(root,text='Anchor Point Finder [BETA]',command=run_anchor_point).grid(row=4,column=0)
tk.Button(root,text='HELP',command=help_button).grid(row=5,column=0)

root.mainloop()
