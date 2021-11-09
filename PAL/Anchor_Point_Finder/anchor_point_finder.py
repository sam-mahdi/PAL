import os



def make_search_list(nhsqc,nhsqc_directory):
    nitrogen_list=[]
    os.chdir(nhsqc_directory)
    with open(nhsqc) as NHSQC_file:
        for lines in NHSQC_file:
            if lines.split() == []:
                continue
            if lines.split()[0] == 'Assignment':
                continue
            nitrogen_value=lines.strip().split()[1]
            nitrogen_list.append(nitrogen_value)
    return nitrogen_list

def search_HNCA(hnca,hnca_directory,nhsqc,nhsqc_directory):
    nitrogen_list=make_search_list(nhsqc,nhsqc_directory)
    alpha_carbon_list=[]
    anchor_point_HNCA_list=[]
    os.chdir(hnca_directory)
    for values in nitrogen_list:
        with open(hnca) as HNCA_file:
            for lines in HNCA_file:
                if lines.split() == []:
                    continue
                if lines.split()[0] == 'Assignment':
                    continue
                alpha_carbon=lines.strip().split()[2]
                nitrogen_value=lines.strip().split()[1]
                if values == nitrogen_value:
                    alpha_carbon_list.append(alpha_carbon)
        if len(alpha_carbon_list) == 2:
            anchor_point_HNCA_list.append(values)
        alpha_carbon_list.clear()
    return anchor_point_HNCA_list

def search_HNCOCA(hnca,hnca_directory,nhsqc,nhsqc_directory,hncoca,hncoca_directory):
    nitrogen_list=make_search_list(nhsqc,nhsqc_directory)
    alpha_carbon_list=[]
    i_1_alpha_carbon_list=[]
    anchor_point_HNCA_list=[]
    i_1_anchor_point_HNCA_list=[]
    for values in nitrogen_list:
        os.chdir(hnca_directory)
        with open(hnca) as HNCA_file:
            for lines in HNCA_file:
                if lines.split() == []:
                    continue
                if lines.split()[0] == 'Assignment':
                    continue
                alpha_carbon=lines.strip().split()[2]
                nitrogen_value=lines.strip().split()[1]
                if values == nitrogen_value:
                    alpha_carbon_list.append(alpha_carbon)
        if len(alpha_carbon_list) > 2:
            alpha_carbon_list.clear()
        os.chdir(hncoca_directory)
        with open(hncoca) as HNCOCA_file:
            for line in HNCACO_file:
                if line.split() == []:
                    continue
                if line.split()[0] == 'Assignment':
                    continue
                i_1_alpha_carbon=lines.strip().split()[2]
                i_1_nitrogen_value=lines.strip().split()[1]
                if values == i_1_nitrogen_value:
                    i_1_alpha_carbon_list.append(i_1_alpha_carbon)
        if len(i_1_alpha_carbon_list) <= 1:
            if len(alpha_carbon_list)+len(i_1_alpha_carbon_list) ==2 or  len(alpha_carbon_list)+len(i_1_alpha_carbon_list) == 3:
                anchor_point_HNCA_list.append(values)
        i_1_alpha_carbon_list.clear()
        alpha_carbon_list.clear()
    return anchor_point_HNCA_list

def search_CBCACONH(nhsqc,nhsqc_directory,hncacb_directory,hncacb,cbcaconh,cbcaconh_directory,CB_only_flag):
    if CB_only_flag.get() != 0:
        number_of_peaks=2
    else:
        number_of_peaks=4
    nitrogen_list=make_search_list(nhsqc,nhsqc_directory)
    beta_carbon_list=[]
    i_1_beta_carbon_list=[]
    anchor_point_HNCACB_list=[]
    for values in nitrogen_list:
        os.chdir(hncacb_directory)
        with open(hncacb) as HNCACB_file:
            for lines in HNCACB_file:
                if lines.split() == []:
                    continue
                if lines.split()[0] == 'Assignment':
                    continue
                beta_carbon=lines.strip().split()[2]
                nitrogen_value=lines.strip().split()[1]
                if values == nitrogen_value:
                    beta_carbon_list.append(beta_carbon)
        if len(beta_carbon_list) > number_of_peaks:
            beta_carbon_list.clear()
        os.chdir(cbcaconh_directory)
        with open(cbcaconh) as CBCACONH_file:
            for line in CBCACONH_file:
                if line.split() == []:
                    continue
                if line.split()[0] == 'Assignment':
                    continue
                i_1_beta_carbon=line.strip().split()[2]
                i_1_nitrogen_value=line.strip().split()[1]
                if values == i_1_nitrogen_value:
                    i_1_beta_carbon_list.append(i_1_beta_carbon)
            if len(i_1_beta_carbon_list) == 2:
                if CB_only_flag.get() != 0:
                    if len(beta_carbon_list)+len(i_1_beta_carbon_list) == 3 or len(beta_carbon_list)+len(i_1_beta_carbon_list) == 4:
                        anchor_point_HNCACB_list.append(values)
                else:
                    if len(beta_carbon_list)+len(i_1_beta_carbon_list) >= 4 or len(beta_carbon_list)+len(i_1_beta_carbon_list) <= 6:
                        anchor_point_HNCACB_list.append(values)
            i_1_beta_carbon_list.clear()
            beta_carbon_list.clear()
    return anchor_point_HNCACB_list




def search_HNCACB(nhsqc,nhsqc_directory,hncacb_directory,hncacb,CB_only_flag):
    if CB_only_flag.get() != 0:
        number_of_peaks=2
    else:
        number_of_peaks=4
    nitrogen_list=make_search_list(nhsqc,nhsqc_directory)
    beta_carbon_list=[]
    anchor_point_HNCACB_list=[]
    os.chdir(hncacb_directory)
    for values in nitrogen_list:
        with open(hncacb) as HNCACB_file:
            for lines in HNCACB_file:
                if lines.split() == []:
                    continue
                if lines.split()[0] == 'Assignment':
                    continue
                beta_carbon=lines.strip().split()[2]
                nitrogen_value=lines.strip().split()[1]
                if values == nitrogen_value:
                    beta_carbon_list.append(beta_carbon)
        if len(beta_carbon_list) == number_of_peaks:
            anchor_point_HNCACB_list.append(values)
        beta_carbon_list.clear()
    return anchor_point_HNCACB_list

def filter_lists(nhsqc,nhsqc_directory,hncacb_directory,hncacb,cbcaconh,cbcaconh_directory,hnca,hnca_directory,hncoca,hncoca_directory,CB_only_flag):
    filtered_list=[]
    if hncoca != ():
        HNCA_list=search_HNCOCA(hnca,hnca_directory,nhsqc,nhsqc_directory,hncoca,hncoca_directory)
    else:
        HNCA_list=search_HNCA(hnca,hnca_directory,nhsqc,nhsqc_directory)
    if cbcaconh != ():
        HNCACB_list=search_CBCACONH(nhsqc,nhsqc_directory,hncacb_directory,hncacb,cbcaconh,cbcaconh_directory,CB_only_flag)
    else:
        HNCACB_list=search_HNCACB(nhsqc,nhsqc_directory,hncacb_directory,hncacb,CB_only_flag)
    for lines in HNCA_list:
        for lines2 in HNCACB_list:
            if lines==lines2:
                filtered_list.append(lines)
    return filtered_list

def make_CA_CB_lists(values,hnca,hnca_directory,hncacb,hncacb_directory,carbon_tolerance,CB_only_flag):
    alpha_carbon_list=[]
    beta_carbon_list=[]
    with open(hnca) as HNCA_file:
        os.chdir(hnca_directory)
        for lines in HNCA_file:
            if lines.split() == []:
                continue
            if lines.split()[0] == 'Assignment':
                continue
            alpha_carbon=lines.strip().split()[2]
            nitrogen_value=lines.strip().split()[1]
            if values == nitrogen_value:
                alpha_carbon_list.append(alpha_carbon)
    with open(hncacb) as HNCACB_file:
        os.chdir(hncacb_directory)
        for line in HNCACB_file:
            if line.split() == []:
                continue
            if line.split()[0] == 'Assignment':
                continue
            beta_carbon=line.strip().split()[2]
            beta_nitrogen_value=line.strip().split()[1]
            if values == beta_nitrogen_value:
                beta_carbon_list.append(beta_carbon)
    if CB_only_flag.get() != 0:
        for entries in alpha_carbon_list:
            for beta_carbons in beta_carbon_list:
                if float(entries) > (float(beta_carbons)-carbon_tolerance) and float(entries) < (float(beta_carbons)+carbon_tolerance):
                    beta_carbon_list.remove(beta_carbons)
    return alpha_carbon_list,beta_carbon_list

def make_COCA_CBCA_lists(values,hnca,hnca_directory,hncacb,hncacb_directory,hncoca,hncoca_directory,cbcaconh,cbcaconh_directory,CB_only_flag,carbon_tolerance,CB_tolerance,filter_CB_flag):
    alpha_carbon_list=[]
    beta_carbon_list=[]
    with open(hnca) as HNCA_file:
        os.chdir(hnca_directory)
        for lines in HNCA_file:
            if lines.split() == []:
                continue
            if lines.split()[0] == 'Assignment':
                continue
            alpha_carbon=lines.strip().split()[2]
            nitrogen_value=lines.strip().split()[1]
            if values == nitrogen_value:
                alpha_carbon_list.append(alpha_carbon)
    if hncoca != ():
        os.chdir(hncoca_directory)
        with open(hncoca) as HNCOCA_file:
            for line in HNCACO_file:
                if line.split() == []:
                    continue
                if line.split()[0] == 'Assignment':
                    continue
                i_1_alpha_carbon=lines.strip().split()[2]
                i_1_nitrogen_value=lines.strip().split()[1]
                if values == i_1_nitrogen_value:
                    if len(alpha_carbon_list) == 1:
                        alpha_carbon_list.append(i_1_alpha_carbon)
    os.chdir(hncacb_directory)
    with open(hncacb) as HNCACB_file:
        for CB_lines in HNCACB_file:
            if CB_lines.split() == []:
                continue
            if CB_lines.split()[0] == 'Assignment':
                continue
            beta_carbon=CB_lines.strip().split()[2]
            beta_nitrogen_value=CB_lines.strip().split()[1]
            if values == beta_nitrogen_value:
                beta_carbon_list.append(beta_carbon)
    if cbcaconh != ():
        os.chdir(cbcaconh_directory)
        with open(cbcaconh) as CBCACONH_file:
            for CB_line in CBCACONH_file:
                if CB_line.split() == []:
                    continue
                if CB_line.split()[0] == 'Assignment':
                    continue
                i_1_beta_carbon=CB_line.split()[2]
                i_1_beta_nitrogen_value=CB_line.split()[1]
                if values == i_1_beta_nitrogen_value:
                    beta_carbon_list.append(i_1_beta_carbon)
    for entries in alpha_carbon_list:
        for beta_carbons in beta_carbon_list:
            if float(entries) > (float(beta_carbons)-carbon_tolerance) and float(entries) < (float(beta_carbons)+carbon_tolerance):
                beta_carbon_list.remove(beta_carbons)
    if filter_CB_flag.get() != 0:
        for beta_carbon1 in beta_carbon_list:
            for beta_carbon in beta_carbon_list:
                if beta_carbon1 == beta_carbon:
                    continue
                if float(beta_carbon1) > (float(beta_carbon)-CB_tolerance) and float(beta_carbon1) < (float(beta_carbon)+CB_tolerance):
                    beta_carbon_list.remove(beta_carbon1)
    return alpha_carbon_list,beta_carbon_list


def search_CA_CB(alpha_carbon_list,beta_carbon_list,values,carbon_tolerance,hnca,hnca_directory,hncacb,hncacb_directory,hncoca,hncoca_directory,cbcaconh,cbcaconh_directory):
    counter=-1
    matched_alpha_carbon_list=[]
    matched_beta_carbon_list=[]
    CA_CB_matches=[[],[],[],[]]
    CA_CB_values=[[],[],[],[]]
    for alpha_carbons in alpha_carbon_list:
        with open(hnca) as HNCA_file:
            for lines in HNCA_file:
                if lines.split() == []:
                    continue
                if lines.split()[0] == 'Assignment':
                    continue
                alpha_carbon=lines.strip().split()[2]
                nitrogen_value=lines.strip().split()[1]
                if values != nitrogen_value and float(alpha_carbon) > (float(alpha_carbons)-carbon_tolerance) and float(alpha_carbon) < (float(alpha_carbons)+carbon_tolerance):
                    matched_alpha_carbon_list.append(nitrogen_value)
        if hncoca != ():
            os.chdir(hncoca_directory)
            with open(hncoca_directory) as hncoca_file:
                for CA_line in hncoca_file:
                    if CA_line.split() == []:
                        continue
                    if CA_line.split()[0] == 'Assignment':
                        continue
                    i_1_alpha_carbon=CA_line.strip().split()[2]
                    i_1_nitrogen_value=CA_line.strip().split()[1]
                    if values != i_1_nitrogen_value and float(i_1_alpha_carbon) > (float(alpha_carbons)-carbon_tolerance) and float(i_1_alpha_carbon) < (float(alpha_carbons)+carbon_tolerance):
                        matched_alpha_carbon_list.append(i_1_nitrogen_value)
        for beta_carbons in beta_carbon_list:
            counter+=1
            with open(hncacb) as HNCACB_file:
                for line in HNCACB_file:
                    if line.split() == []:
                        continue
                    if line.split()[0] == 'Assignment':
                        continue
                    beta_carbon=line.strip().split()[2]
                    beta_nitrogen_value=line.strip().split()[1]
                    if values != beta_nitrogen_value and  float(beta_carbon) > (float(beta_carbons)-carbon_tolerance) and float(beta_carbon) < (float(beta_carbons)+carbon_tolerance):
                        matched_beta_carbon_list.append(beta_nitrogen_value)
            if cbcaconh != ():
                os.chdir(cbcaconh_directory)
                with open(cbcaconh) as CBCACONH_file:
                    for CB_line in CBCACONH_file:
                        if CB_line.split() == []:
                            continue
                        if CB_line.split()[0] == 'Assignment':
                            continue
                        i_1_beta_carbon=CB_line.split()[2]
                        i_1_beta_nitrogen_value=CB_line.split()[1]
                        if values != i_1_beta_nitrogen_value and  float(i_1_beta_carbon) > (float(beta_carbons)-carbon_tolerance) and float(i_1_beta_carbon) < (float(beta_carbons)+carbon_tolerance):
                            matched_beta_carbon_list.append(i_1_beta_nitrogen_value)
            CA_CB_values[counter].append(f'{alpha_carbons} {beta_carbons}')
            for matches in matched_alpha_carbon_list:
                if matches in matched_beta_carbon_list:
                    CA_CB_matches[counter].append(f'{matches}')
            matched_beta_carbon_list.clear()
        matched_alpha_carbon_list.clear()
    return CA_CB_values,CA_CB_matches


def label_matches(filtered_list,nhsqc,nhsqc_directory):
    labels_list=[]
    for values in filtered_list:
        os.chdir(nhsqc_directory)
        with open(nhsqc) as nhsqc_file:
            for lines in nhsqc_file:
                if lines.split() == []:
                    continue
                if lines.split()[0] == 'Assignment':
                    continue
                labels=lines.strip().split()[0]
                nitrogen_value=lines.strip().split()[1]
                if values == nitrogen_value:
                    labels_list.append(labels)
    return labels_list





def find_i_min_plus_1_matches(nhsqc,nhsqc_directory,hncacb_directory,hncacb,cbcaconh,cbcaconh_directory,hnca,hnca_directory,hncoca,hncoca_directory,carbon_tolerance,CB_tolerance,CB_only_flag,filter_CB_flag,with_strip_plot):
    filtered_list=filter_lists(nhsqc,nhsqc_directory,hncacb_directory,hncacb,cbcaconh,cbcaconh_directory,hnca,hnca_directory,hncoca,hncoca_directory,CB_only_flag)
    labels_list=label_matches(filtered_list,nhsqc,nhsqc_directory)
    count=0
    if with_strip_plot is True:
        import pandas as pd
        new_format=pd.DataFrame(columns=list(['Label','i','CA','CB','Matches']))
        for values,labels in zip(filtered_list,labels_list):
            if hncoca != '' or cbcaconh != '':
                alpha_carbon_list,beta_carbon_list=make_COCA_CBCA_lists(values,hnca,hnca_directory,hncacb,hncacb_directory,hncoca,hncoca_directory,cbcaconh,cbcaconh_directory,CB_only_flag,carbon_tolerance,CB_tolerance,filter_CB_flag)
            else:
                alpha_carbon_list,beta_carbon_list=make_CA_CB_lists(values,hnca,hnca_directory,hncacb,hncacb_directory,carbon_tolerance,CB_only_flag)
            if len(alpha_carbon_list)+len(beta_carbon_list) == 4:
                CA_CB_values,CA_CB_matches =search_CA_CB(alpha_carbon_list,beta_carbon_list,values,carbon_tolerance,hnca,hnca_directory,hncacb,hncacb_directory,hncoca,hncoca_directory,cbcaconh,cbcaconh_directory)
                for CA_CB,matches in zip(CA_CB_values,CA_CB_matches):
                    if matches != []:
                        new_format=new_format.append({'Label':labels,'i':values,'CA':(" ".join(CA_CB)).split()[0],'CB':(" ".join(CA_CB)).split()[1],'Matches':" ".join(matches)},ignore_index=True)
        new_format.loc[new_format.duplicated(subset='i'),'i']= ' '
        new_format.loc[new_format.duplicated(subset='Label'),'Label']= ' '
        new_format.to_csv('csv_output.csv',index=False)
    else:
        with open('i_and_i_minus_1_matches_only.txt','w') as write_file:
            write_file.write('Amide values of peaks with both i and i-1 CA and CB values\n')
            for labels,values in zip(labels_list,filtered_list):
                write_file.write(labels+ ': '+values+'\n')
