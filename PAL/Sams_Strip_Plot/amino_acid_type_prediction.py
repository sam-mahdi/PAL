import re
import re

def inputed_variables_count(carbon_alpha,carbon_beta,carbon_carbonyl,nitrogen_amide,hydrogen_amide):
    """Users may input a variety of variables, sometimes CA and CO, sometimes CA CB, sometimes only CA, to make sure only matches that contain the proper number of atoms (i.e. matches that match both CA and CO
    , here I define a count that will be used to filter matches)"""
    count=0
    for variables in locals().values():
        if variables != 0:
            count+=1
    return count



def all_backbone_atoms(carbon_alpha,carbon_beta,carbon_carbonyl,nitrogen_amide,hydrogen_amide):
    """
    This will go through each amino acid set, and create lists depending on what matches it found. Since each amino acid only has one CA, CB, CO, etc. The number of matches should equal the number of inputed variables.
    If they do, then the matches are put into a list, then written into an output.txt file if users want to see the chemical shift values and std for their matches. Output of function is just a list of the atoms"""
    count=inputed_variables_count(carbon_alpha,carbon_beta,carbon_carbonyl,nitrogen_amide,hydrogen_amide)
    residue_list=[]
    carbon_alpha_list=[]
    carbon_beta_list=[]
    carbon_carbonyl_list=[]
    nitrogen_amide_list=[]
    hydrogen_amide_list=[]
    matches_list=[]
    atom_matches=[]
    counter=0
    if hydrogen_amide != 0:
        hydrogen_flag=True
    with open('bmrb.csv') as file:
        for lines in file:
            if lines == '\n':
                continue
            split_lines=lines.split(',')
            residue=split_lines[0]
            if residue == 'comp_id':
                continue
            residue_list.append(residue)
            atom=split_lines[1]
            chemical_shift=float(split_lines[5])
            std=float(split_lines[6])
            lower_half=chemical_shift-std
            upper_half=chemical_shift+std
            if residue_list[0] != residue or (residue+atom) == 'VALN':
                if len(carbon_alpha_list)+len(carbon_beta_list)+len(hydrogen_amide_list)+len(nitrogen_amide_list)+len(carbon_carbonyl_list) == count:
                    alpha_carbon=' '.join(carbon_alpha_list)
                    beta_carbon=' '.join(carbon_beta_list)
                    hydrogen_amide_atom=' '.join(hydrogen_amide_list)
                    nitrogen_amide_atom=' '.join(nitrogen_amide_list)
                    carbonyl=' '.join(carbon_carbonyl_list)
                    if f'{alpha_carbon} {beta_carbon} {hydrogen_amide_atom} {nitrogen_amide_atom} {carbonyl}\n' in matches_list:
                        continue
                    else:
                        counter+=1
                        matches_list.append(f'\nMatch {counter}:\n')
                        matches_list.append(f'{alpha_carbon} {beta_carbon} {hydrogen_amide_atom} {nitrogen_amide_atom} {carbonyl}\n')
                carbon_alpha_list.clear()
                carbon_beta_list.clear()
                carbon_carbonyl_list.clear()
                nitrogen_amide_list.clear()
                hydrogen_amide_list.clear()
                residue_list.clear()
                residue_list.append(residue)
                if hydrogen_amide>lower_half and hydrogen_amide<upper_half:
                    hydrogen_amide_list.append(f'{residue} {atom} {chemical_shift} {std}')

            if carbon_alpha>lower_half and carbon_alpha<upper_half and atom == 'CA':
                carbon_alpha_list.append(f'{residue} {atom} {chemical_shift} {std}')
            if carbon_beta>lower_half and carbon_beta<upper_half and atom == 'CB':
                carbon_beta_list.append(f'{residue} {atom} {chemical_shift} {std}')
            if carbon_carbonyl>lower_half and carbon_carbonyl<upper_half and atom == 'C':
                carbon_carbonyl_list.append(f'{residue} {atom} {chemical_shift} {std}')
            if nitrogen_amide>lower_half and nitrogen_amide<upper_half and atom == 'N':
                nitrogen_amide_list.append(f'{residue} {atom} {chemical_shift} {std}')
            if hydrogen_amide>lower_half and hydrogen_amide<upper_half and atom == 'H':
                if hydrogen_flag is True:
                    continue
                hydrogen_amide_list.append(f'{residue} {atom} {chemical_shift} {std}')
        with open('output.txt','w') as write_file:
            write_file.write(f'Values inputted:\nAlpha Carbon: {carbon_alpha}\nBeta Carbon: {carbon_beta}\nCaonyl: {carbon_carbonyl}\nNitrogen: {nitrogen_amide}\nHydrogen: {hydrogen_amide}\n')
            for lines in matches_list:
                if lines.split()[0] != 'Match':
                    atom_matches.append(lines.split()[0])
                    write_file.write(lines.replace(f' {lines.split()[0]}',f'\n{lines.split()[0]}'))
                else:
                    write_file.write(lines)
        return atom_matches

def inputed_variables_count(carbon_alpha,carbon_beta,carbon_carbonyl,nitrogen_amide,hydrogen_amide):
    count=0
    for variables in locals().values():
        if variables != 0:
            count+=1
    return count



def all_backbone_atoms(carbon_alpha,carbon_beta,carbon_carbonyl,nitrogen_amide,hydrogen_amide):
    """
    This will go through each amino acid, and check its carbon_alpha and carbon_beta coordinates.
    If they are within the user inputed range, it will store these in the lists.
    Upon completing an amino acid, it will then go through all the matches, and print them out accordingly"""
    count=inputed_variables_count(carbon_alpha,carbon_beta,carbon_carbonyl,nitrogen_amide,hydrogen_amide)
    residue_list=[]
    carbon_alpha_list=[]
    carbon_beta_list=[]
    carbon_carbonyl_list=[]
    nitrogen_amide_list=[]
    hydrogen_amide_list=[]
    matches_list=[]
    atom_matches=[]
    counter=0
    if hydrogen_amide != 0:
        hydrogen_flag=True
    with open('bmrb.csv') as file:
        for lines in file:
            if lines == '\n':
                continue
            split_lines=lines.split(',')
            residue=split_lines[0]
            if residue == 'comp_id':
                continue
            residue_list.append(residue)
            atom=split_lines[1]
            chemical_shift=float(split_lines[5])
            std=float(split_lines[6])
            lower_half=chemical_shift-std
            upper_half=chemical_shift+std
            if residue_list[0] != residue or (residue+atom) == 'VALN':
                if len(carbon_alpha_list)+len(carbon_beta_list)+len(hydrogen_amide_list)+len(nitrogen_amide_list)+len(carbon_carbonyl_list) == count:
                    alpha_carbon=' '.join(carbon_alpha_list)
                    beta_carbon=' '.join(carbon_beta_list)
                    hydrogen_amide_atom=' '.join(hydrogen_amide_list)
                    nitrogen_amide_atom=' '.join(nitrogen_amide_list)
                    carbonyl=' '.join(carbon_carbonyl_list)
                    if f'{alpha_carbon} {beta_carbon} {hydrogen_amide_atom} {nitrogen_amide_atom} {carbonyl}\n' in matches_list:
                        continue
                    else:
                        counter+=1
                        matches_list.append(f'\nMatch {counter}:\n')
                        matches_list.append(f'{alpha_carbon} {beta_carbon} {hydrogen_amide_atom} {nitrogen_amide_atom} {carbonyl}\n')
                carbon_alpha_list.clear()
                carbon_beta_list.clear()
                carbon_carbonyl_list.clear()
                nitrogen_amide_list.clear()
                hydrogen_amide_list.clear()
                residue_list.clear()
                residue_list.append(residue)
                if hydrogen_amide>lower_half and hydrogen_amide<upper_half:
                    hydrogen_amide_list.append(f'{residue} {atom} {chemical_shift} {std}')

            if carbon_alpha>lower_half and carbon_alpha<upper_half and atom == 'CA':
                carbon_alpha_list.append(f'{residue} {atom} {chemical_shift} {std}')
            if carbon_beta>lower_half and carbon_beta<upper_half and atom == 'CB':
                carbon_beta_list.append(f'{residue} {atom} {chemical_shift} {std}')
            if carbon_carbonyl>lower_half and carbon_carbonyl<upper_half and atom == 'C':
                carbon_carbonyl_list.append(f'{residue} {atom} {chemical_shift} {std}')
            if nitrogen_amide>lower_half and nitrogen_amide<upper_half and atom == 'N':
                nitrogen_amide_list.append(f'{residue} {atom} {chemical_shift} {std}')
            if hydrogen_amide>lower_half and hydrogen_amide<upper_half and atom == 'H':
                if hydrogen_flag is True:
                    continue
                hydrogen_amide_list.append(f'{residue} {atom} {chemical_shift} {std}')
        with open('output.txt','w') as write_file:
            write_file.write(f'Values inputted:\nAlpha Carbon: {carbon_alpha}\nBeta Carbon: {carbon_beta}\nCaonyl: {carbon_carbonyl}\nNitrogen: {nitrogen_amide}\nHydrogen: {hydrogen_amide}\n')
            for lines in matches_list:
                #write_file.write(lines)
                if lines.split()[0] != 'Match':
                    atom_matches.append(lines.split()[0])
                    write_file.write(lines.replace(f' {lines.split()[0]}',f'\n{lines.split()[0]}'))
                else:
                    write_file.write(lines)
        return atom_matches
