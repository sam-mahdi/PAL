from tkinter import *
import tkinter.scrolledtext as st
from tkinter import ttk
import functools
import os
from tkinter import filedialog
import os

root = Tk()
root.title('Anchor Point Finder [IN BETA]')
root.geometry('800x600')

class ReadOnlyText(st.ScrolledText):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.config(state=DISABLED)

        self.insert = self._unlock(super().insert)
        self.delete = self._unlock(super().delete)

    def _unlock(self, f):
        @functools.wraps(f)
        def wrap(*args, **kwargs):
            self.config(state=NORMAL)
            r = f(*args, **kwargs)
            self.config(state=DISABLED)
            return r
        return wrap


ttk.Label(root,text = "Program Output",font = ("Times New Roman", 15),background = 'green',foreground = "white").grid(column = 1, row = 17)
text_area = ReadOnlyText(root,width = 60,height = 15,font = ("Times New Roman",12))
text_area.grid(column = 0,columnspan=3,sticky=W+E,pady = 10, padx = 10,row=19)

nhsqc=()
nhsqc_directory=()
hnca=()
hnca_directory=()
hncacb=()
hncacb_directory=()
hncoca=()
hncoca_directory=()
nhsqc=()
nhsqc_directory=()
cbcaconh=()
cbcaconh_directory=()

carbon_tolerance=()
CB_tolerance=()


CB_only_flag = IntVar()
filter_CB_flag = IntVar()

Label(root, text='NHSQC').grid(row=0, sticky=W)
Label(root, text='HNCA').grid(row=1, sticky=W)
Label(root, text='HNCACB').grid(row=2, sticky=W)
Label(root, text='HNCOCA').grid(row=3, sticky=W)
Label(root, text='CBCACONH').grid(row=4, sticky=W)
Label(root, text='Carbon Tolerance').grid(row=5, sticky=W)
Label(root, text='CB Tolerance').grid(row=6, sticky=W)

nhsqc_line=Entry(root)
nhsqc_line.grid(row=0,column=1,sticky=W)
hnca_line=Entry(root)
hnca_line.grid(row=1,column=1,sticky=W)
hncacb_line=Entry(root)
hncacb_line.grid(row=2,column=1,sticky=W)
hncoca_line=Entry(root)
hncoca_line.grid(row=3,column=1,sticky=W)
cbcaconh_line=Entry(root)
cbcaconh_line.grid(row=4,column=1,sticky=W)
carbon_tolerance_line=Entry(root)
carbon_tolerance_line.grid(row=5,column=1,sticky=W)
cb_tolerance_line=Entry(root)
cb_tolerance_line.grid(row=6,column=1,sticky=W)

def input_nhsqc():
    fullpath = filedialog.askopenfilename(parent=root, title='Choose a file')
    global nhsqc
    global nhsqc_directory
    nhsqc_directory=os.path.dirname(fullpath)
    nhsqc= os.path.basename(fullpath)
    label3=Label(root,text=fullpath).grid(row=0,column=1)

def input_hnca():
    fullpath = filedialog.askopenfilename(parent=root, title='Choose a file')
    global hnca
    global hnca_directory
    hnca_directory=os.path.dirname(fullpath)
    hnca= os.path.basename(fullpath)
    label3=Label(root,text=fullpath).grid(row=1,column=1)

def input_hncacb():
    fullpath = filedialog.askopenfilename(parent=root, title='Choose a file')
    global hncacb
    global hncacb_directory
    hncacb_directory=os.path.dirname(fullpath)
    hncacb= os.path.basename(fullpath)
    label3=Label(root,text=fullpath).grid(row=2,column=1)

def input_hncoca():
    fullpath = filedialog.askopenfilename(parent=root, title='Choose a file')
    global hncoca
    global hncoca_directory
    hncoca_directory=os.path.dirname(fullpath)
    hncoca= os.path.basename(fullpath)
    label3=Label(root,text=fullpath).grid(row=3,column=1)

def input_cbcaconh():
    fullpath = filedialog.askopenfilename(parent=root, title='Choose a file')
    global cbcaconh
    global cbcaconh_directory
    cbcaconh_directory=os.path.dirname(fullpath)
    cbcaconh= os.path.basename(fullpath)
    label3=Label(root,text=fullpath).grid(row=4,column=1)

def get_carbon_tolerance():
    global carbon_tolerance
    if carbon_tolerance_line.get() == '':
        carbon_tolerance=()
    else:
        carbon_tolerance=float(carbon_tolerance_line.get())

def get_CB_tolerance():
    global CB_tolerance
    if cb_tolerance_line.get() == '':
        CB_tolerance=()
    else:
        CB_tolerance=float(cb_tolerance_line.get())

def run_without_matches():
    global nhsqc
    global nhsqc_directory
    global hnca
    global hnca_directory
    global hncacb
    global hncacb_directory
    global hncoca
    global hncoca_directory
    global cbcaconh
    global cbcaconh_directory
    if nhsqc == '':
        nhsqc=()
        nhsqc_directory=()
    if hnca == '':
        hnca=()
        hnca_directory=()
    if hncacb == '':
        hncacb=()
        hncacb_directory=()
    if hncoca == '':
        hncoca=()
        hncoca_directory=()
    if cbcaconh == '':
        cbcaconh=()
        cbcaconh_directory=()
    if nhsqc == ():
        text_area.insert(INSERT, 'Error: NHSQC File Missing, please upload an HNCA file\n')
    elif hnca == ():
        text_area.insert(INSERT, 'Error: HNCA File Missing, please upload an HNCA file\n')
    elif hncacb == ():
        text_area.insert(INSERT, 'Error: HNCACB File Missing, please upload an HNCA file\n')
    else:
        text_area.insert(INSERT, 'Program Start\n Running Anchor Point Finder without Matches\n')
        root.update_idletasks()
        import anchor_point_finder as apf
        with_strip_plot=False
        apf.find_i_min_plus_1_matches(nhsqc,nhsqc_directory,hncacb_directory,hncacb,cbcaconh,cbcaconh_directory,hnca,hnca_directory,hncoca,hncoca_directory,carbon_tolerance,CB_tolerance,CB_only_flag,filter_CB_flag,with_strip_plot)
        text_area.insert(INSERT, 'Program End\n')

def run_with_matches():
    global nhsqc
    global nhsqc_directory
    global hnca
    global hnca_directory
    global hncacb
    global hncacb_directory
    global hncoca
    global hncoca_directory
    global cbcaconh
    global cbcaconh_directory
    if nhsqc == '':
        nhsqc=()
    if hnca == '':
        hnca=()
        hnca_directory=()
    if hncacb == '':
        hncacb=()
        hncacb_directory=()
    if hncoca == '':
        hncoca=()
        hncoca_directory=()
    if cbcaconh == '':
        cbcaconh=()
        cbcaconh_directory=()
    if nhsqc == ():
        text_area.insert(INSERT, 'Error: NHSQC File Missing, please upload an HNCA file\n')
    elif hnca == ():
        text_area.insert(INSERT, 'Error: HNCA File Missing, please upload an HNCA file\n')
    elif hncacb == ():
        text_area.insert(INSERT, 'Error: HNCACB File Missing, please upload an HNCA file\n')
    elif carbon_tolerance == ():
        text_area.insert(INSERT, 'Error: Carbon Tolerance Missing [make sure to click enter]\n')
    elif filter_CB_flag.get() != 0 and CB_tolerance == ():
        text_area.insert(INSERT, 'Error: CB Tolerance Missing, but filter CB box has been checked. Please add CB tolerance or unclick the box [make sure to click enter]\n')
    else:
        if CB_tolerance != () and filter_CB_flag.get() == 0:
            text_area.insert(INSERT, 'Warning: CB Tolerance Value is entered, but the box is unchecked\n')
        text_area.insert(INSERT, 'Program Start\n Running Anchor Point Finder with Matches\n')
        root.update_idletasks()
        import anchor_point_finder as apf
        with_strip_plot=True
        apf.find_i_min_plus_1_matches(nhsqc,nhsqc_directory,hncacb_directory,hncacb,cbcaconh,cbcaconh_directory,hnca,hnca_directory,hncoca,hncoca_directory,carbon_tolerance,CB_tolerance,CB_only_flag,filter_CB_flag,with_strip_plot)
        text_area.insert(INSERT, 'Program End\n')




Button(root, text='Browse', command=input_nhsqc).grid(row=0,column=2, sticky=W)
Button(root, text='Browse', command=input_hnca).grid(row=1,column=2, sticky=W)
Button(root, text='Browse', command=input_hncacb).grid(row=2,column=2, sticky=W)
Button(root, text='Browse', command=input_hncoca).grid(row=3,column=2, sticky=W)
Button(root, text='Browse', command=input_cbcaconh).grid(row=4,column=2, sticky=W)
Button(root, text='Enter', command=get_carbon_tolerance).grid(row=5,column=2, sticky=W)
Button(root, text='Enter', command=get_CB_tolerance).grid(row=6,column=2, sticky=W)
Button(root, text='Run Without Matches', command=run_without_matches).grid(row=7,column=1, sticky=W)
Button(root, text='Run With Matches', command=run_with_matches).grid(row=8,column=1, sticky=W)
Checkbutton(root, text="CB Optimized HNCACB", variable=CB_only_flag).grid(row=7,column=0, sticky=W)
Checkbutton(root, text="Filter CB", variable=filter_CB_flag).grid(row=8,column=0, sticky=W)

mainloop()
