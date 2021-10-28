from tkinter import *
from tkinter import filedialog
import os
import re

hnca=()
hnca_directory=()
hncacb=()
hncacb_directory=()
hnco=()
hnco_directory=()
hncaco=()
hncaco_directory=()
hncoca=()
hncoca_directory=()
NOE=()
NOE_directory=()
nhsqc=()
nhsqc_directory=()
old_nhsqc=()
old_nhsqc_directory=()

unassigned_flag1= IntVar()
transfer_only_CB_HNCACB1= IntVar()


class newTopLevel(object):
    def __init__(self, root):
        self.newWindow = Toplevel(root)
        self.newWindow.title("Peaklist Files")
        self.newWindow.geometry("600x600")
        Label(self.newWindow, text="HNCA File\n Use Browse Button").grid(row=0)
        self.pdb_line = Entry(self.newWindow)
        self.pdb_line.grid(row=0, column=1)
        self.newWindow.btn = Button(self.newWindow,text='browse',command=self.input_hnca)
        self.newWindow.btn.grid(row=0,column=2)
        Label(self.newWindow, text="HNCACB File\n Use Browse Button").grid(row=1)
        self.pdb_start_line = Entry(self.newWindow)
        self.pdb_start_line.grid(row=1, column=1)
        self.newWindow.btn = Button(self.newWindow,text='browse',command=self.input_hncacb)
        self.newWindow.btn.grid(row=1,column=2)
        Label(self.newWindow, text="HNCO File\n Use Browse Button").grid(row=2)
        self.pdb_end_line = Entry(self.newWindow)
        self.pdb_end_line.grid(row=2, column=1)
        self.newWindow.btn = Button(self.newWindow,text='browse',command=self.input_hnco)
        self.newWindow.btn.grid(row=2,column=2)
        Label(self.newWindow, text="HNCOCA File\n Use Browse Button").grid(row=3)
        self.pdb_chain_line = Entry(self.newWindow)
        self.pdb_chain_line.grid(row=3, column=1)
        self.newWindow.btn = Button(self.newWindow,text='browse',command=self.input_hncoca)
        self.newWindow.btn.grid(row=3,column=2)
        Label(self.newWindow, text="HNCACO File\n Use Browse Button").grid(row=4)
        self.pdb_chain_line = Entry(self.newWindow)
        self.pdb_chain_line.grid(row=4, column=1)
        self.newWindow.btn = Button(self.newWindow,text='browse',command=self.input_hncaco)
        self.newWindow.btn.grid(row=4,column=2)
        Label(self.newWindow, text="NOE File\n Use Browse Button").grid(row=5)
        self.pdb_chain_line = Entry(self.newWindow)
        self.pdb_chain_line.grid(row=5, column=1)
        self.newWindow.btn = Button(self.newWindow,text='browse',command=self.input_NOE)
        self.newWindow.btn.grid(row=5,column=2)
        Label(self.newWindow, text="Peaklist File Converter").grid(row=6,column=1)
        Label(self.newWindow, text="New NHSQC File\n Use Browse Button").grid(row=7)
        self.pdb_chain_line = Entry(self.newWindow)
        self.pdb_chain_line.grid(row=7, column=1)
        self.newWindow.btn = Button(self.newWindow,text='browse',command=self.input_nhsqc)
        self.newWindow.btn.grid(row=7,column=2)
        Label(self.newWindow, text="Old NHSQC File\n Use Browse Button").grid(row=8)
        self.pdb_chain_line = Entry(self.newWindow)
        self.pdb_chain_line.grid(row=8, column=1)
        self.newWindow.btn = Button(self.newWindow,text='browse',command=self.input_old_nhsqc)
        self.newWindow.btn.grid(row=8,column=2)
        self.newWindow.btn=Checkbutton(self.newWindow, text="Transfer Unassigned Peaks", variable=unassigned_flag1)
        self.newWindow.btn.grid(row=9,column=1, sticky=W)
        self.newWindow.btn=Checkbutton(self.newWindow, text="Transfer Only CBs in HNCACB", variable=transfer_only_CB_HNCACB1)
        self.newWindow.btn.grid(row=9,column=2, sticky=W)
        self.newWindow.btn = Button(self.newWindow,text='Convert',command=self.run)
        self.newWindow.btn.grid(row=10,column=1)


    def input_hnca(self):
        fullpath = filedialog.askopenfilename(parent=self.newWindow, title='Choose a file')
        global hnca
        global hnca_directory
        hnca_directory=os.path.dirname(fullpath)
        hnca= os.path.basename(fullpath)
        label3=Label(self.newWindow,text=fullpath).grid(row=0,column=1)
    def input_hncacb(self):
        fullpath = filedialog.askopenfilename(parent=self.newWindow, title='Choose a file')
        global hncacb
        global hncacb_directory
        hncacb_directory=os.path.dirname(fullpath)
        hncacb= os.path.basename(fullpath)
        label3=Label(self.newWindow,text=fullpath).grid(row=1,column=1)
    def input_hnco(self):
        fullpath = filedialog.askopenfilename(parent=self.newWindow, title='Choose a file')
        global hnco
        global hnco_directory
        hnco_directory=os.path.dirname(fullpath)
        hnco= os.path.basename(fullpath)
        label3=Label(self.newWindow,text=fullpath).grid(row=2,column=1)
    def input_hncoca(self):
        fullpath = filedialog.askopenfilename(parent=self.newWindow, title='Choose a file')
        global hncoca
        global hncoca_directory
        hncoca_directory=os.path.dirname(fullpath)
        hncoca= os.path.basename(fullpath)
        label3=Label(self.newWindow,text=fullpath).grid(row=3,column=1)
    def input_hncaco(self):
        fullpath = filedialog.askopenfilename(parent=self.newWindow, title='Choose a file')
        global hncaco
        global hncaco_directory
        hncaco_directory=os.path.dirname(fullpath)
        hncaco= os.path.basename(fullpath)
        label3=Label(self.newWindow,text=fullpath).grid(row=4,column=1)
    def input_NOE(self):
        fullpath = filedialog.askopenfilename(parent=self.newWindow, title='Choose a file')
        global NOE
        global NOE_directory
        NOE_directory=os.path.dirname(fullpath)
        NOE= os.path.basename(fullpath)
        label3=Label(self.newWindow,text=fullpath).grid(row=5,column=1)
    def input_nhsqc(self):
        fullpath = filedialog.askopenfilename(parent=self.newWindow, title='Choose a file')
        global nhsqc
        global nhsqc_directory
        nhsqc_directory=os.path.dirname(fullpath)
        nhsqc= os.path.basename(fullpath)
        label3=Label(self.newWindow,text=fullpath).grid(row=7,column=1)
    def input_old_nhsqc(self):
        fullpath = filedialog.askopenfilename(parent=self.newWindow, title='Choose a file')
        global old_nhsqc
        global old_nhsqc_directory
        old_nhsqc_directory=os.path.dirname(fullpath)
        old_nhsqc= os.path.basename(fullpath)
        label3=Label(self.newWindow,text=fullpath).grid(row=8,column=1)
    def run(self):
        unassigned_flag = unassigned_flag1.get()
        transfer_only_CB_HNCACB = transfer_only_CB_HNCACB1.get()
        from assignment_shifter import main
        main(nhsqc,nhsqc_directory,hnca,hnca_directory,hncacb,hncacb_directory,hnco,hnco_directory,hncoca,hncoca_directory,old_nhsqc,old_nhsqc_directory,NOE,NOE_directory,hncaco,hncaco_directory,unassigned_flag,transfer_only_CB_HNCACB)

def variables():
    return hnca,hnca_directory,hncacb, hncacb_directory, hnco, hnco_directory, hncaco, hncaco_directory, hncoca, hncoca_directory, NOE, NOE_directory
