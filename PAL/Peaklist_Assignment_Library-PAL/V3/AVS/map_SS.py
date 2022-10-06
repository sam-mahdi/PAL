from pymol import cmd, stored, math
import pymol
import os
import sys
import re

def pymol_mapSS(NMRSTAR_directory,pdb_file,pdb_directory,startaa):
    ss_dict={'L':0,'H':2,'E':1,'X':0}
    convert={'R':'ARG','H':'HIS','K':'LYS','D':'ASP','E':'GLU','S':'SER','T':'THR','N':'ASN','Q':'GLN','C':'CYS','G':'GLY','P':'PRO','A':'ALA','V':'VAL','I':'ILE','L':'LEU','W':'TRP','Y':'TYR','F':'PHE','M':'MET'}
    ss_only=[]
    residue_type=[]
    residue_number=[]
    pymol.finish_launching()
    os.chdir(pdb_directory)
    cmd.load(pdb_file)
    mol=pdb_file[0:-4]
    os.chdir(NMRSTAR_directory)
    with open('predSS.tab') as ss_file:
        for lines in ss_file:
            searcher=re.search('^\d+',lines.strip())
            if searcher != None:
            	if lines.strip().split()[1] == 'X':
            		continue
            	ss_only.append(ss_dict[lines.strip().split()[8]])
            	residue_number.append(lines.strip().split()[0])
            	residue_type.append(convert[lines.strip().split()[1]])
    obj=cmd.get_object_list(mol)
    cmd.alter(mol,"b=-1.0")
    bfacts=[]
    for ss,residue,residuen in zip(ss_only,residue_type,residue_number):
    	print(ss,residue,residuen)
    for ss,residue,residuen in zip(ss_only,residue_type,residue_number):
        bfact=float(ss)
        cmd.alter("%s and resi %s and resn %s and n. CA"%(mol,residuen,residue), "b=%s"%bfact)
    cmd.cartoon("automatic",mol)
    cmd.spectrum("b","grey grey blue red", "%s and n. CA " %mol)
    cmd.recolor()

pymol_mapSS(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4])
