from pymol import cmd, stored, math
import pymol
import os
import sys
import re

def pymol_mapS2(NMRSTAR_directory,pdb_file,pdb_directory,startaa):
    s2_only=[]
    residue_type=[]
    residue_number=[]
    convert={'R':'ARG','H':'HIS','K':'LYS','D':'ASP','E':'GLU','S':'SER','T':'THR','N':'ASN','Q':'GLN','C':'CYS','G':'GLY','P':'PRO','A':'ALA','V':'VAL','I':'ILE','L':'LEU','W':'TRP','Y':'TYR','F':'PHE','M':'MET'}
    pymol.finish_launching()
    os.chdir(pdb_directory)
    cmd.load(pdb_file)
    mol=pdb_file[0:-4]
    os.chdir(NMRSTAR_directory)
    with open('predS2.tab') as s2_file:
        for lines in s2_file:
            searcher=re.search('\d+\.\d{3}',lines)
            if searcher != None:
                if lines.strip().split()[1] == 'X':
                    continue
                s2_only.append(searcher.group(0))
                residue_number.append(lines.strip().split()[0])
                residue_type.append(convert[lines.strip().split()[1]])
    obj=cmd.get_object_list(mol)
    bfacts=[]
    s2_list=[]
    for entries in s2_only:
        if float(entries) > 1:
            continue
        s2_list.append(float(entries))
    average=sum(s2_list)/len(s2_list)
    default_value=((1/(float(average)))-float(average))/1.5
    cmd.alter(mol,"b=%s"%default_value)    
    for line,residue,residuen in zip(s2_only,residue_type,residue_number):
        if float(line) > 1:
            bfact=default_value
        else:    
            bfact=((1/(float(line)))-float(line))/1.5
        bfacts.append(bfact)
        cmd.alter("%s and resi %s and resn %s and n. CA"%(mol,residuen,residue), "b=%s"%bfact)
    cmd.show_as("cartoon",mol)
    cmd.cartoon("putty", mol)
    cmd.set("cartoon_putty_scale_min", min(bfacts),mol)
    cmd.set("cartoon_putty_scale_max", max(bfacts),mol)
    cmd.set("cartoon_putty_transform", 7,mol)
    cmd.set("cartoon_putty_radius", max(bfacts),mol)
    cmd.spectrum("b","white red", "%s and n. CA " %mol)
    cmd.ramp_new("color_bar", mol, [max(s2_list), min(s2_list)],["white","red"])
    cmd.recolor()

pymol_mapS2(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4])
