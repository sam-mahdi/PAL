import re
import os

new_hnca=[]
new_hnco=[]
new_hncacb=[]
new_hncoca=[]
new_NOE=[]
new_hncaco=[]

unassigned_hnca=[]
unassigned_hnco=[]
unassigned_hncacb=[]
unassigned_hncoca=[]
unassigned_hncaco=[]
unassigned_NOE=[]


def make_name_list(nhsqc,hnca,hncacb,hnco,hncoca,NOE,hncaco,old_nhsqc):
    list_of_names=[]
    list_of_names2=[]
    if hnca != ():
        list_of_names.append(hnca)
        list_of_names2.append('hnca')
    if hncacb != ():
        list_of_names.append(hncacb)
        list_of_names2.append('hncacb')
    if hnco != ():
        list_of_names.append(hnco)
        list_of_names2.append('hnco')
    if hncoca != ():
        list_of_names.append(hncoca)
        list_of_names2.append('hncoca')
    if NOE != () and old_nhsqc != ():
        list_of_names.append(NOE)
        list_of_names2.append('NOE')
    if hncaco != ():
        list_of_names.append(hncaco)
        list_of_names2.append('hncaco')
    return list_of_names,list_of_names2

def shift_3d(new_nhsqc_file,nhsqc,nhsqc_directory,hnca,hnca_directory,hncacb,hncacb_directory,hnco,hnco_directory,hncoca,hncoca_directory,old_nhsqc,old_nhsqc_directory,NOE,NOE_directory,hncaco,hncaco_directory,unassigned_flag,transfer_only_CB_HNCACB):
    for lines in new_nhsqc_file:
        if lines.split() == []:
            continue
        if lines.strip().split()[0] == 'Assignment':
            continue
        assigned_peaks=re.search('([A-Z]\d+)N-',lines)
        if assigned_peaks != None:
            nitrogen_value=lines.strip().split()[1]
            hydrogen_value=lines.strip().split()[2]
            residue=assigned_peaks.group(1)
            if hnca != ():
                os.chdir(hnca_directory)
                hnca_shift(hnca,unassigned_flag,residue,hydrogen_value,nitrogen_value)
            if hncacb != ():
                os.chdir(hncacb_directory)
                hncacb_shift(hncacb,unassigned_flag,transfer_only_CB_HNCACB,residue,hydrogen_value,nitrogen_value)
            if hnco != ():
                os.chdir(hnco_directory)
                hnco_shift(hnco,unassigned_flag,residue,hydrogen_value,nitrogen_value)
            if hncoca != ():
                os.chdir(hncoca_directory)
                hncoca_shift(hncoca,unassigned_flag,residue,hydrogen_value,nitrogen_value)
            if NOE != () and old_nhsqc != ():
                NOE_shift(unassigned_flag,old_nhsqc,old_nhsqc_directory,NOE,NOE_directory,residue,hydrogen_value,nitrogen_value)

def hnca_shift(hnca,unassigned_flag,residue,hydrogen_value,nitrogen_value):
    with open(hnca) as hnca_file:
        for lines in hnca_file:
            if lines.split() == []:
                continue
            if lines.strip().split()[0] == 'Assignment':
                continue
            if unassigned_flag != 0:
                check_unassigned=re.search('\?\-\?',lines)
                if check_unassigned != None and lines not in unassigned_hnca:
                    unassigned_hnca.append(lines)
            assigned_peaks=re.search('[A-Z]\d+',lines)
            if assigned_peaks != None:
                if residue == assigned_peaks.group(0):
                    amino_acid = lines.strip().split()[0]
                    carbon_value=lines.strip().split()[2]
                    new_hnca.append(f'{amino_acid}\t{nitrogen_value}\t{carbon_value}\t{hydrogen_value}\n')
def hncacb_shift(hncacb,unassigned_flag,transfer_only_CB_HNCACB,residue,hydrogen_value,nitrogen_value):
    with open(hncacb) as hncacb_file:
        for lines in hncacb_file:
            if lines.split() == []:
                continue
            if lines.strip().split()[0] == 'Assignment':
                continue
            assigned_peaks=re.search('[A-Z]\d+',lines)
            if unassigned_flag != 0:
                check_unassigned=re.search('\?\-\?',lines)
                if check_unassigned != None and lines not in unassigned_hncacb:
                    unassigned_hncacb.append(lines)
            if transfer_only_CB_HNCACB != 0:
                alpha_check=re.search('CA',lines)
                if alpha_check != None:
                    continue
            if assigned_peaks != None:
                if residue == assigned_peaks.group(0):
                    amino_acid = lines.strip().split()[0]
                    carbon_value=lines.strip().split()[2]
                    new_hncacb.append(f'{amino_acid}\t{nitrogen_value}\t{carbon_value}\t{hydrogen_value}\n')
def hnco_shift(hnco,unassigned_flag,residue,hydrogen_value,nitrogen_value):
    with open(hnco) as hnco_file:
        for lines in hnco_file:
            if lines.split() == []:
                continue
            if lines.strip().split()[0] == 'Assignment':
                continue
            if unassigned_flag != 0:
                check_unassigned=re.search('\?\-\?',lines)
                if check_unassigned != None and lines not in unassigned_hnco:
                    unassigned_hnco.append(lines)
            assigned_peaks=re.search('[A-Z]\d+',lines)
            if assigned_peaks != None:
                if residue == assigned_peaks.group(0):
                    amino_acid = lines.strip().split()[0]
                    carbon_value=lines.strip().split()[2]
                    new_hnco.append(f'{amino_acid}\t{nitrogen_value}\t{carbon_value}\t{hydrogen_value}\n')

def hncoca_shift(hncoca,unassigned_flag,residue,hydrogen_value,nitrogen_value):
    with open(hncoca) as hncoca_file:
        for lines in hncoca_file:
            if lines.split() == []:
                continue
            if lines.strip().split()[0] == 'Assignment':
                continue
            if unassigned_flag != 0:
                check_unassigned=re.search('\?\-\?',lines)
                if check_unassigned != None and lines not in unassigned_hncoca:
                    unassigned_hncoca.append(lines)
            assigned_peaks=re.search('[A-Z]\d+',lines)
            if assigned_peaks != None:
                if residue == assigned_peaks.group(0):
                    amino_acid = lines.strip().split()[0]
                    carbon_value=lines.strip().split()[2]
                    new_hncoca.append(f'{amino_acid}\t{nitrogen_value}\t{carbon_value}\t{hydrogen_value}\n')

def hncaco_shift(hncaco,unassigned_flag,residue,hydrogen_value,nitrogen_value):
    with open(hncaco) as hncaco_file:
        for lines in hncaco_file:
            if lines.split() == []:
                continue
            if lines.strip().split()[0] == 'Assignment':
                continue
            if unassigned_flag != 0:
                check_unassigned=re.search('\?\-\?',lines)
                if check_unassigned != None and lines not in unassigned_hncaco:
                    unassigned_hncaco.append(lines)
            assigned_peaks=re.search('[A-Z]\d+',lines)
            if assigned_peaks != None:
                if residue == assigned_peaks.group(0):
                    amino_acid = lines.strip().split()[0]
                    carbon_value=lines.strip().split()[2]
                    new_hncaco.append(f'{amino_acid}\t{nitrogen_value}\t{carbon_value}\t{hydrogen_value}\n')

def NOE_shift(unassigned_flag,old_nhsqc,old_nhsqc_directory,NOE,NOE_directory,residue,hydrogen_value,nitrogen_value):
    os.chdir(old_nhsqc_directory)
    with open(old_nhsqc) as old_nhsqc_file:
        for lines in old_nhsqc_file:
            if lines.split() == []:
                continue
            if lines.strip().split()[0] == 'Assignment':
                continue
            assigned_peaks=re.search('[A-Z]\d+',lines)
            if assigned_peaks != None:
                if residue == assigned_peaks.group(0):
                    old_nitrogen_value=lines.strip().split()[1]
                    os.chdir(NOE_directory)
                    with open(NOE) as NOE_file:
                        for line in NOE_file:
                            if line.split() == []:
                                continue
                            if line.strip().split()[0] == 'Assignment':
                                continue
                            noe_nitrogen=line.strip().split()[1]
                            noe_nitrogen_match=line.strip().split()[2]
                            label=line.strip().split()[0]
                            if noe_nitrogen == old_nitrogen_value:
                                new_NOE.append(f'{label}\t{nitrogen_value}\t{noe_nitrogen_match}\t{hydrogen_value}\n')
            else:
                if unassigned_flag != 0:
                    old_nitrogen_value=lines.strip().split()[1]
                    os.chdir(NOE_directory)
                    with open(NOE) as NOE_file:
                        for line in NOE_file:
                            if line.split() == []:
                                continue
                            if line.strip().split()[0] == 'Assignment':
                                continue
                            noe_nitrogen=line.strip().split()[1]
                            if noe_nitrogen == old_nitrogen_value and line not in unassigned_NOE:
                                unassigned_NOE.append(line)


def clear_lists():
    new_hnca.clear()
    new_hnco.clear()
    new_hncacb.clear()
    new_hncoca.clear()
    new_NOE.clear()
    new_hncaco.clear()

    unassigned_hnca.clear()
    unassigned_hnco.clear()
    unassigned_hncacb.clear()
    unassigned_hncoca.clear()
    unassigned_hncaco.clear()
    unassigned_NOE.clear()


def main(nhsqc,nhsqc_directory,hnca,hnca_directory,hncacb,hncacb_directory,hnco,hnco_directory,hncoca,hncoca_directory,old_nhsqc,old_nhsqc_directory,NOE,NOE_directory,hncaco,hncaco_directory,unassigned_flag,transfer_only_CB_HNCACB):
    clear_lists()
    os.chdir(nhsqc_directory)
    with open(nhsqc) as new_nhsqc_file:
        shift_3d(new_nhsqc_file,nhsqc,nhsqc_directory,hnca,hnca_directory,hncacb,hncacb_directory,hnco,hnco_directory,hncoca,hncoca_directory,old_nhsqc,old_nhsqc_directory,NOE,NOE_directory,hncaco,hncaco_directory,unassigned_flag,transfer_only_CB_HNCACB)
    list_of_names,list_of_names2=make_name_list(nhsqc,hnca,hncacb,hnco,hncoca,NOE,hncaco,old_nhsqc)
    for entries,names in zip(list_of_names,list_of_names2):
        with open('new'+entries,'w') as file:
            file.write('Assignment\tw1\tw2\tw3\n')
            if unassigned_flag != 0:
                name='unassigned_'+names
                for values in globals()[name]:
                    file.write(values)
            list_name='new_'+names
            for lines in globals()[list_name]:
                file.write(lines)
