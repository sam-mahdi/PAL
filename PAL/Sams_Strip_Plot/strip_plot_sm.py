from tkinter import *
import tkinter.scrolledtext as st
from tkinter import ttk
import functools
import os

root = Tk()
root.title('Strip Plot')

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


ttk.Label(root,text = "Program Output",font = ("Times New Roman", 15),background = 'green',foreground = "white").grid(column = 1, row = 16)
ttk.Label(root,text = "Strip Plot Matches",font = ("Times New Roman", 12)).grid(column = 0, row = 17)
ttk.Label(root,text = "Amino Acid Identity",font = ("Times New Roman", 12)).grid(column = 2, row = 17)

text_area = ReadOnlyText(root,width = 30,height = 15,font = ("Times New Roman",12))

matches_text_area = ReadOnlyText(root,width = 30,height = 15,font = ("Times New Roman",12))

text_area.grid(column = 0,columnspan=2,sticky=W+E,pady = 10, padx = 10,row=18)

matches_text_area.grid(column = 2,sticky=W+E,pady = 10, padx = 10,row=18)

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

i_minus_CA=()
i_minus_CB=()
i_minus_CO=()
i_nitrogen=()
i_amide_hydrogen=()

Label(root, text='Carbon Tolerance').grid(row=1, sticky=W)
Label(root, text='Hydrogen_tolerance').grid(row=2, sticky=W)
Label(root, text='CA Value').grid(row=3, sticky=W)
Label(root, text='CB Value').grid(row=4, sticky=W)
Label(root, text='CO Value').grid(row=5, sticky=W)
Label(root, text='Nitrogen Value').grid(row=6, sticky=W)
Label(root, text='NH Value').grid(row=7, sticky=W)

carbon_tolerance_value=Entry(root)
carbon_tolerance_value.grid(row=1,column=1,sticky=W)
hydrogen_tolerance_value=Entry(root)
hydrogen_tolerance_value.grid(row=2,column=1,sticky=W)
CA_tolerance_value=Entry(root)
CA_tolerance_value.grid(row=3,column=1,sticky=W)
CB_tolerance_value=Entry(root)
CB_tolerance_value.grid(row=4,column=1,sticky=W)
CO_tolerance_value=Entry(root)
CO_tolerance_value.grid(row=5,column=1,sticky=W)
nitrogen_tolerance_value=Entry(root)
nitrogen_tolerance_value.grid(row=6,column=1,sticky=W)
amide_hydrogen_tolerance_value=Entry(root)
amide_hydrogen_tolerance_value.grid(row=7,column=1,sticky=W)

carbon_tolerance=()
hydrogen_tolerance=()
counter=0

def get_carbon_tolerance():
    global carbon_tolerance
    if carbon_tolerance_value.get() == '':
        carbon_tolerance=()
    else:
        carbon_tolerance=float(carbon_tolerance_value.get())

def get_hydrogen_tolerance():
    global hydrogen_tolerance
    if hydrogen_tolerance_value.get() == '':
        hydrogen_tolerance=()
    else:
        hydrogen_tolerance=float(hydrogen_tolerance_value.get())

def get_CA():
    global i_minus_CA
    if CA_tolerance_value.get() == '':
        i_minus_CA=()
    else:
        i_minus_CA=float(CA_tolerance_value.get())

def get_CB():
    global i_minus_CB
    if CB_tolerance_value.get() == '':
        i_minus_CB=()
    else:
        i_minus_CB=float(CB_tolerance_value.get())

def get_CO():
    global i_minus_CO
    if CO_tolerance_value.get() == '':
        i_minus_CO=()
    else:
        i_minus_CO=float(CO_tolerance_value.get())

def get_nitrogen():
    global i_nitrogen
    if nitrogen_tolerance_value.get() == '':
        i_nitrogen=()
    else:
        i_nitrogen=float(nitrogen_tolerance_value.get())

def get_amide_hydrogen():
    global i_amide_hydrogen
    if amide_hydrogen_tolerance_value.get() == '':
        i_amide_hydrogen=()
    else:
        i_amide_hydrogen=float(amide_hydrogen_tolerance_value.get())


CA_only_flag = IntVar()
CA_CB_flag = IntVar()
CA_CO_flag = IntVar()
CA_CB_CO_flag = IntVar()
i_CA_flag = IntVar()
for_CA_CO_flag = IntVar()
i_CA_CA_flag = IntVar()
CA_CO_i_CA_flag = IntVar()
for_CA_CB_CO_flag = IntVar()
CA_CB_i_CA_flag = IntVar()
CA_CB_CO_i_CA_flag = IntVar()
NH_flag = IntVar()
HA_flag = IntVar()
exclude_nitrogen_identity_search_flag= IntVar()

display_carbon_matches_flag = IntVar()
display_NH_NOE_flag = IntVar()
display_HA_NOE_flag = IntVar()
display_combined_NH_HA_NOE_flag = IntVar()



def peaklist_window():
    from peak_list_window import newTopLevel
    new_top = newTopLevel(root)
    newWindow = new_top.newWindow

def clear():
    text_area.delete(1.0,END)

def clear():
    global counter
    counter=0
    matches_text_area.delete(1.0,END)



NOE_NH=[]
NOE_HA=[]
i_NOE=[]

"""i-1 matches"""
CA_matches=[]
CA_CB_matches=[]
CO_matches=[]
CA_CO_matches=[]
CA_CB_CO_matches=[]
NOE_NH_matches=[]
NOE_HA_matches=[]

"""i+1 matches"""
i_CA_matches=[]
i_CA_CA_matches=[]
CA_CO_i_CA_matches=[]
CA_CB_i_CA_matches=[]
CA_CB_CO_i_CA_matches=[]



def HNCA_match():
    global CA_matches
    if hnca == ():
        text_area.insert(INSERT, 'Error: HNCA Peaklist File Missing, make sure to use browse to upload it\n')
        return
    if i_minus_CA == ():
        text_area.insert(INSERT, 'Error: CA Value Missing, make sure to use enter to add it\n')
        return
    os.chdir(hnca_directory)
    with open(hnca) as hnca_file:
        for lines in hnca_file:
            if lines == '' or lines == '\n':
                continue
            if lines.strip().split()[0]=='Assignment':
                continue
            nitrogen_value=float(lines.strip().split()[1])
            CA_value=float(lines.strip().split()[2])
            if CA_value > (i_minus_CA-carbon_tolerance) and CA_value < (i_minus_CA+carbon_tolerance):
                CA_matches.append(nitrogen_value)

def HNCACB_match():
    global CA_CB_matches
    if hncacb == ():
        text_area.insert(INSERT, 'Error: HNCACB Peaklist File Missing, make sure to use browse to upload it\n')
        return
    if i_minus_CB == ():
        text_area.insert(INSERT, 'Error: CB Value Missing, make sure to use enter to add it\n')
        return
    os.chdir(hncacb_directory)
    for entries in CA_matches:
        with open(hncacb) as hncacb_file:
            for lines in hncacb_file:
                if lines == '' or lines == '\n':
                    continue
                if lines.split() == []:
                    continue
                if lines.strip().split()[0]=='Assignment':
                    continue
                nitrogen_value=float(lines.strip().split()[1])
                CB_value=float(lines.strip().split()[2])
                if nitrogen_value == entries:
                    if CB_value > (i_minus_CB-carbon_tolerance) and CB_value < (i_minus_CB+carbon_tolerance):
                        CA_CB_matches.append(nitrogen_value)


def HNCACO():
    global CO_matches
    if hncaco == ():
        text_area.insert(INSERT, 'Error: HNCACO Peaklist File Missing, make sure to use browse to upload it\n')
        return
    if i_minus_CO == ():
        text_area.insert(INSERT, 'Error: CO Value Missing, make sure to use enter to add it\n')
        return
    os.chdir(hncaco_directory)
    with open(hncaco) as hnco_file:
        for lines in hnco_file:
            if lines == '' or lines == '\n':
                continue
            if lines.strip().split()[0]=='Assignment':
                continue
            nitrogen_value=float(lines.strip().split()[1])
            CO_value=float(lines.strip().split()[2])
            if CO_value > (i_minus_CO-carbon_tolerance) and CO_value < (i_minus_CO+carbon_tolerance):
                CO_matches.append(nitrogen_value)

def HNCOCA():
    global i_CA_matches
    if hncoca == ():
        text_area.insert(INSERT, 'Error: HNCOCA Peaklist File Missing, make sure to use browse to upload it\n')
        return
    if i_minus_CA == ():
        text_area.insert(INSERT, 'Error: CA Value Missing, make sure to use enter to add it\n')
        return
    os.chdir(hncoca_directory)
    with open(hncoca) as hncoca_file:
        for lines in hncoca_file:
            if lines == '' or lines == '\n':
                continue
            if lines.strip().split()[0]=='Assignment':
                continue
            nitrogen_value=float(lines.strip().split()[1])
            i_CA_value=float(lines.strip().split()[2])
            if i_CA_value > (i_minus_CA-carbon_tolerance) and i_CA_value < (i_minus_CA+carbon_tolerance):
                i_CA_matches.append(nitrogen_value)

def i_HNCO():
    global CO_matches
    if hnco == ():
        text_area.insert(INSERT, 'Error: HNCO Peaklist File Missing, make sure to use browse to upload it\n')
        return
    if i_minus_CO == ():
        text_area.insert(INSERT, 'Error: CO Value Missing, make sure to use enter to add it\n')
        return
    os.chdir(hnco_directory)
    with open(hnco) as hnco_file:
        for lines in hnco_file:
            if lines == '' or lines == '\n':
                continue
            if lines.strip().split()[0]=='Assignment':
                continue
            nitrogen_value=float(lines.strip().split()[1])
            CO_value=float(lines.strip().split()[2])
            if CO_value > (i_minus_CO-carbon_tolerance) and CO_value < (i_minus_CO+carbon_tolerance):
                CO_matches.append(nitrogen_value)


def HNCOCA_HNCA():
    for entries in i_CA_matches:
        for values in CA_matches:
            if entries == values:
                i_CA_CA_matches.append(entries)

def HNCA_HNCACO_HNCOCA():
    global CA_CO_i_CA_matches
    for entries in CA_CO_matches:
        for values in i_CA_matches:
            if entries == values:
                CA_CO_i_CA_matches.append(entries)

def HNCA_HNCACO():
    global CA_CO_matches
    for entries in CA_matches:
        for values in CO_matches:
            if entries == values:
                CA_CO_matches.append(entries)

def HNCA_CB_HNCACO():
    global CA_CB_CO_matches
    for entries in CA_CB_matches:
        for values in CO_matches:
            if entries == values:
                CA_CB_CO_matches.append(entries)

def HNCA_CB_i_CA():
    global CA_CB_i_CA_matches
    for entries in CA_CB_matches:
        for values in i_CA_matches:
            if entries == values:
                CA_CB_i_CA_matches.append(entries)

def HNCA_CB_CO_i_CA():
    global CA_CB_CO_i_CA_matches
    for entries in CA_CB_CO_matches:
        for values in i_CA_matches:
            if entries == values:
                CA_CB_CO_i_CA_matches.append(entries)

def NOE_matches(list):
    global NOE_NH
    global NOE_HA
    if NOE == ():
        text_area.insert(INSERT, 'Error: NOE Peaklist File Missing, make sure to use browse to upload it\n')
        return
    os.chdir(NOE_directory)
    for entries in list:
        with open(NOE) as noe_file:
            for lines in noe_file:
                if lines == '' or lines == '\n':
                    continue
                if lines.strip().split()[0]=='Assignment':
                    continue
                nitrogen=float(lines.strip().split()[1])
                hydrogen=float(lines.strip().split()[2])
                if entries == nitrogen:
                    if hydrogen < 12 and hydrogen > 6:
                        NOE_NH.append(str(nitrogen)+' '+str(hydrogen))
                    if hydrogen < 6 and hydrogen > 3.5:
                        NOE_HA.append(str(nitrogen)+' '+str(hydrogen))

def i_noes():
    global i_NOE
    if NOE == ():
        text_area.insert(INSERT, 'Error: NOE Peaklist File Missing, make sure to use browse to upload it\n')
        return
    with open(NOE) as noe_file:
        for lines in noe_file:
            if lines == '' or lines == '\n':
                continue
            if lines.strip().split()[0]=='Assignment':
                continue
            nitrogen=float(lines.strip().split()[1])
            hydrogen=float(lines.strip().split()[2])
            if nitrogen == i_nitrogen:
                i_NOE.append(hydrogen)

def NOE_i_NH_match():
    global NOE_NH_matches
    for values in i_NOE:
        for entries in NOE_NH:
            nitrogen=float(entries.split()[0])
            hydrogen=float(entries.split()[1])
            if hydrogen > (values-hydrogen_tolerance) and hydrogen < (values+hydrogen_tolerance):
                if nitrogen not in NOE_NH_matches:
                    NOE_NH_matches.append(nitrogen)
def NOE_i_HA_match():
    global NOE_HA_matches
    for values in i_NOE:
        for entries in NOE_HA:
            nitrogen=float(entries.split()[0])
            hydrogen=float(entries.split()[1])
            if hydrogen > (values-hydrogen_tolerance) and hydrogen < (values+hydrogen_tolerance):
                if nitrogen not in NOE_HA_matches:
                    NOE_HA_matches.append(nitrogen)

def run():
    global hnca,hnca_directory,hncacb, hncacb_directory, hnco, hnco_directory, hncaco, hncaco_directory, hncoca, hncoca_directory, NOE, NOE_directory
    from peak_list_window import variables
    hnca,hnca_directory,hncacb, hncacb_directory, hnco, hnco_directory, hncaco, hncaco_directory, hncoca, hncoca_directory, NOE, NOE_directory = variables()
    if carbon_tolerance == ():
        text_area.insert(INSERT, 'Error: Carbon Tolerance Value Missing, make sure to use enter to add it\n')
        return
    if hydrogen_tolerance == ():
        text_area.insert(INSERT, 'Error: Hydrogen Tolerance Value Missing, make sure to use enter to add it\n')
        return
    if i_nitrogen == ():
        text_area.insert(INSERT, 'Error: Nitrogen Value Missing, make sure to use enter to add it\n')
        return
    list_of_variables=[i_nitrogen,i_minus_CA,i_minus_CB,i_minus_CO]
    list_of_variable_names=['Nitrogen','CA carbon','CB Carbon','CO Carbon']
    for variables,names in zip(list_of_variables,list_of_variable_names):
        if variables == ():
            continue
        text_area.insert(INSERT, f'Values Used {names}: {variables}\n')
    if CA_only_flag.get() != 0:
        text_area.insert(INSERT, 'CA Only\n')
        HNCA_match()
        list=CA_matches
        if display_carbon_matches_flag.get() != 0:
            for entries in CA_matches:
                text_area.insert(INSERT,str(entries)+'\n')
    if CA_CB_flag.get() != 0:
        text_area.insert(INSERT, 'CA and CB\n')
        HNCA_match()
        HNCACB_match()
        list=CA_CB_matches
        if display_carbon_matches_flag.get() != 0:
            for entries in CA_CB_matches:
                text_area.insert(INSERT, str(entries)+'\n')
    if CA_CO_flag.get() != 0:
        text_area.insert(INSERT, 'CA and CO\n')
        HNCA_match()
        HNCACO()
        HNCA_HNCACO()
        list=CA_CO_matches
        if display_carbon_matches_flag.get() != 0:
            for entries in CA_CO_matches:
                text_area.insert(INSERT,str(entries)+'\n')
    if CA_CB_CO_flag.get() != 0:
        text_area.insert(INSERT, 'CA, CB, and CO\n')
        HNCA_match()
        HNCACO()
        HNCACB_match()
        HNCA_CB_HNCACO()
        list=CA_CB_CO_matches
        if display_carbon_matches_flag.get() != 0:
            for entries in CA_CB_CO_matches:
                text_area.insert(INSERT,str(entries)+'\n')
    if i_CA_flag.get() != 0:
        text_area.insert(INSERT, 'i_CA [HNCOCA]\n')
        HNCOCA()
        list=i_CA_matches
        if display_carbon_matches_flag.get() != 0:
            for entries in i_CA_matches:
                text_area.insert(INSERT,str(entries)+'\n')
    if i_CA_CA_flag.get() != 0:
        text_area.insert(INSERT, 'HNCOCA and CA\n')
        HNCA_match()
        HNCOCA()
        HNCOCA_HNCA()
        list=i_CA_CA_matches
        if display_carbon_matches_flag.get() != 0:
            for entries in i_CA_CA_matches:
                text_area.insert(INSERT,str(entries)+'\n')
    if for_CA_CO_flag.get() != 0:
        text_area.insert(INSERT, 'CA and CO')
        HNCA_match()
        i_HNCO()
        HNCA_HNCACO()
        list=CA_CO_matches
        if display_carbon_matches_flag.get() != 0:
            for entries in CA_CO_matches:
                text_area.insert(INSERT,str(entries)+'\n')
    if CA_CO_i_CA_flag.get() != 0:
        text_area.insert(INSERT, 'CA, CO, and HNCOCA\n')
        HNCA_match()
        i_HNCO()
        HNCA_HNCACO()
        HNCA_HNCACO_HNCOCA()
        list=CA_CO_i_CA_matches
        if display_carbon_matches_flag.get() != 0:
            for entries in CA_CO_i_CA_matches:
                text_area.insert(INSERT,str(entries)+'\n')
    if for_CA_CB_CO_flag.get() != 0:
        text_area.insert(INSERT, 'CA, CB, CO\n')
        HNCA_match()
        HNCACB_match()
        i_HNCO()
        HNCA_CB_HNCACO()
        list=CA_CB_CO_matches
    if CA_CB_i_CA_flag.get() != 0:
        text_area.insert(INSERT, 'CA, CB, HNCOCA\n')
        HNCA_match()
        HNCACB_match()
        HNCOCA()
        HNCA_CB_i_CA()
        list=CA_CB_i_CA_matches
        if display_carbon_matches_flag.get() != 0:
            for entries in CA_CB_i_CA_matches:
                text_area.insert(INSERT,str(entries)+'\n')
    if CA_CB_CO_i_CA_flag.get() != 0:
        text_area.insert(INSERT, 'CA, CB, CO, HNCOCA\n')
        HNCA_match()
        HNCACB_match()
        i_HNCO()
        HNCA_CB_HNCACO()
        HNCOCA()
        HNCA_CB_CO_i_CA()
        list=CA_CB_CO_i_CA_matches
        if display_carbon_matches_flag.get() != 0:
            for entries in CA_CB_CO_i_CA_matches:
                text_area.insert(INSERT,str(entries)+'\n')
    if NH_flag.get() != 0:
        i_noes()
        NOE_matches(list)
        NOE_i_NH_match()
        if display_NH_NOE_flag.get() != 0:
            text_area.insert(INSERT, 'NOE_NH_Matches\n')
            for entries in NOE_NH_matches:
                text_area.insert(INSERT, str(entries) + '\n')
    if HA_flag.get() != 0:
        i_noes()
        NOE_matches(list)
        NOE_i_HA_match()
        if display_HA_NOE_flag.get() != 0:
            text_area.insert(INSERT, 'NOE_HA_Matches\n')
            for entries in NOE_HA_matches:
                text_area.insert(INSERT, str(entries)+'\n')
    if display_combined_NH_HA_NOE_flag.get() != 0:
        text_area.insert(INSERT, 'NH and HA combined\n')
        for entries in set.intersection(set(NOE_HA_matches),set(NOE_NH_matches)):
            text_area.insert(INSERT, str(entries)+'\n')
    clear_lists()

def clear_lists():
    NOE_NH.clear()
    NOE_HA.clear()
    i_NOE.clear()
    CA_matches.clear()
    CA_CB_matches.clear()
    CO_matches.clear()
    CA_CO_matches.clear()
    CA_CB_CO_matches.clear()
    NOE_NH_matches.clear()
    NOE_HA_matches.clear()
    i_CA_matches.clear()
    i_CA_CA_matches.clear()
    CA_CO_i_CA_matches.clear()
    CA_CB_i_CA_matches.clear()
    CA_CB_CO_i_CA_matches.clear()

def identify_search():
    global counter
    global i_minus_CO
    global i_amide_hydrogen
    global i_nitrogen
    global i_minus_CA
    global i_minus_CB
    import amino_acid_type_prediction as aatp
    if i_minus_CA == () and i_minus_CB == () and i_minus_CO == () and i_amide_hydrogen == () and i_nitrogen == ():
        matches_text_area.insert(INSERT,'Please Enter at least one atom value for matching')
    else:
        counter+=1
        if i_minus_CA == ():
            i_minus_CA=0
        if i_minus_CB == ():
            i_minus_CB=0
        if i_minus_CO == ():
            i_minus_CO=0
        if i_amide_hydrogen == ():
            i_amide_hydrogen=0
        if i_nitrogen == ():
            i_nitrogen=0
        if exclude_nitrogen_identity_search_flag.get() != 0:
            i_nitrogen=0
        identity_list=aatp.all_backbone_atoms(i_minus_CA,i_minus_CB,i_minus_CO,i_nitrogen,i_amide_hydrogen)
        name_list=['CA','CB','CO','N','NH']
        value_list=[i_minus_CA,i_minus_CB,i_minus_CO,i_nitrogen,i_amide_hydrogen]
        matches_text_area.insert(INSERT,f'\nID Match: {counter}\n')
        for names,values in zip(name_list,value_list):
            if values != 0:
                matches_text_area.insert(INSERT,f'{names}: {values}\n')
        for values in identity_list:
            matches_text_area.insert(INSERT,values.split()[0]+'\n')

Button(root, text='Upload Peaklist Files', command=peaklist_window).grid(row=0,column=1, sticky =W)
Button(root, text='Enter', command=get_carbon_tolerance).grid(row=1,column=2, sticky=W)
Button(root, text='Enter', command=get_hydrogen_tolerance).grid(row=2,column=2, sticky=W)
Button(root, text='Enter', command=get_CA).grid(row=3,column=2, sticky=W)
Button(root, text='Enter', command=get_CB).grid(row=4,column=2, sticky=W)
Button(root, text='Enter', command=get_CO).grid(row=5,column=2, sticky=W)
Button(root, text='RUN', command=run).grid(row=13,column=2, sticky=W)
Button(root, text='Clear Matches', command=clear).grid(row=14,column=2, sticky=W)
Button(root, text='Clear Identity', command=clear).grid(row=14,column=2, sticky=E)
Button(root, text='Enter', command=get_nitrogen).grid(row=6,column=2, sticky=W)
Button(root, text='Enter', command=get_amide_hydrogen).grid(row=7,column=2, sticky=W)
Button(root, text='Identify', command=identify_search).grid(row=13,column=2)
Label(root,text='Backward').grid(row=8,column=0, sticky=W)
Checkbutton(root, text="CA only", variable=CA_only_flag).grid(row=9,column=0, sticky=W)
Checkbutton(root, text="CA CB", variable=CA_CB_flag).grid(row=10,column=0, sticky=W)
Checkbutton(root, text="CA CO", variable=CA_CO_flag).grid(row=11,column=0, sticky=W)
Checkbutton(root, text="CA CB CO", variable=CA_CB_CO_flag).grid(row=12,column=0, sticky=W)
Checkbutton(root, text="Exclude Nitrogen in Identity Search", variable=exclude_nitrogen_identity_search_flag).grid(row=6,column=2,sticky=E)
Label(root,text='NOEs').grid(row=13,column=0, sticky=W)
Checkbutton(root, text="NH NOE", variable=NH_flag).grid(row=14,column=0, sticky=W)
Checkbutton(root, text="HA NOE", variable=HA_flag).grid(row=15,column=0, sticky=W)
Label(root,text='Forward').grid(row=8,column=1,sticky=W)
Checkbutton(root, text="HNCOCA only", variable=i_CA_flag).grid(row=9,column=1, sticky=W)
Checkbutton(root, text="CA CO", variable=for_CA_CO_flag).grid(row=10,column=1, sticky=W)
Checkbutton(root, text="CA CB CO", variable=for_CA_CB_CO_flag).grid(row=11,column=1, sticky=W)
Checkbutton(root, text="CA and HNCOCA", variable=i_CA_CA_flag).grid(row=12,column=1, sticky=W)
Checkbutton(root, text="CA CO and HNCOCA", variable=CA_CO_i_CA_flag).grid(row=13,column=1, sticky=W)
Checkbutton(root, text="CA CB and HNCOCA", variable=CA_CB_i_CA_flag).grid(row=14,column=1, sticky=W)
Checkbutton(root, text="CA CB CO and HNCOCA", variable=CA_CB_CO_i_CA_flag).grid(row=15,column=1, sticky=W)
Checkbutton(root, text="Display Carbon Matches", variable=display_carbon_matches_flag).grid(row=9,column=2, sticky=W)
Checkbutton(root, text="Display NH NOE Matches", variable=display_NH_NOE_flag).grid(row=10,column=2, sticky=W)
Checkbutton(root, text="Display HA NOE Matches", variable=display_HA_NOE_flag).grid(row=11,column=2, sticky=W)
Checkbutton(root, text="Display combined NOEs", variable=display_combined_NH_HA_NOE_flag).grid(row=12,column=2, sticky=W)

mainloop()
