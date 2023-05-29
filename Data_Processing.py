import pandas as pd
import numpy as np
import time


def Init_data():
    element_dict = {'atoms': 0
               ,'bonds': 0
               ,'angles': 0
               ,'torsions': 0
               ,'improper': 0 
               ,'dihedrals': 0
               ,'improper_count': 0}

    styl_dict = {'atoms_style': 0
                ,'bonds_style': 0
                ,'angles_style': 0
                ,'torsions_style': 0
                ,'improper_style': 0
                ,'dihedrals_style':0}
                
    return element_dict, styl_dict

def Get_data(element_dict, styl_dict, data_mmol):
    Counter(element_dict, data_mmol)
    data_dict = {'Atoms_data': Save_Atoms_data(element_dict, data_mmol)
                ,'Bonds_data': Save_Bonds_data(element_dict, data_mmol)
                ,'Angles_data': Save_Angles_data(element_dict, data_mmol)
                ,'Dihedrals_data': Save_Dihedrals_data(element_dict, data_mmol) 
                ,'Improper_data': Save_improper_data(element_dict, data_mmol)
                ,'Torsions_data': Save_Torsions_data(element_dict, data_mmol)}
    
    styl_dict = {'atoms_style': len(Atoms_Style(data_dict['Atoms_data']))
                ,'bonds_style': len(Bonds_Style(data_dict['Bonds_data']))
                ,'angles_style': len(Angles_Style(data_dict['Angles_data']))
                ,'torsions_style': len(Torsions_Style(data_dict['Torsions_data']))
                ,'improper_style': len(Improper_Style(data_dict['Improper_data']))
                ,'dihedrals_style': len(Dihedrals_Style(data_dict['Dihedrals_data']))}
    
    return data_dict
    
def Counter(element_dict, data):
    for i in range(data.index.stop):
        value = data[0][i]
        if 'of atoms' in value:
            element_dict['atoms'] = int(data[0][i+1].split()[0])
        elif 'of bonds' in value:
            element_dict['bonds'] = int(data[0][i+1].split()[0])
        elif 'of angles' in value:
            element_dict['angles'] = int(data[0][i+1].split()[0])
        elif 'of torsions' in value:
            element_dict['torsions'] = int(data[0][i+1].split()[0])
        elif 'of dihedrals' in value:
            element_dict['dihedrals'] = int(data[0][i+1].split()[0])
        elif ' improper' in value:
            element_dict['improper_count'] = element_dict['improper_count'] + 1
    Counter_Judgment(element_dict)
    
    
def Counter_Judgment(element_dict):
    if element_dict['improper_count'] != 0:
        element_dict['improper'] = element_dict['improper_count'] - 1
        
def Save_Atoms_data(element_dict, data):
    atoms_value = []
    for i in range(data.index.stop):
        value = data[0][i]
        if element_dict['atoms'] != 0:
            if 'of atoms' in value:
                atoms_index = i
                if 'epsilon' in data[0][atoms_index + 2]:
                    for j in range(element_dict['atoms']):
                        atoms_value.append(data[0][atoms_index + 4 + j])
                else:
                    for j in range(element_dict['atoms']):
                        atoms_value.append(data[0][atoms_index + j + 2])
    return pd.DataFrame(atoms_value)   
    
def Save_Bonds_data(element_dict, data):
    bonds_value = []
    for i in range(data.index.stop):
        value = data[0][i]
        if element_dict['bonds'] != 0:
            if 'of bonds' in value:
                bonds_index = i
                if 'kr(kcal' in data[0][bonds_index + 2]:
                    for j in range(element_dict['bonds']):
                        bonds_value.append(data[0][bonds_index + 3 + j])
                else:
                    pass
    return pd.DataFrame(bonds_value)   
    
    
def Save_Angles_data(element_dict, data):
    angles_value = []
    for i in range(data.index.stop):
        value = data[0][i]
        if element_dict['angles'] != 0:
            if 'of angles' in value:
                angles_index = i
                if 'c1' in data[0][angles_index + 2]:
                    for j in range(element_dict['angles']):
                        angles_value.append(data[0][angles_index + 3 + j])
                else:
                    pass
    return pd.DataFrame(angles_value)   
    
def Save_Dihedrals_data(element_dict, data):
    dihedrals_value = []
    for i in range(data.index.stop):
        value = data[0][i]
        if element_dict['dihedrals'] != 0:
            if 'of dihedrals' in value:
                dihedrals_index = i
                if 'V4' in data[0][dihedrals_index + 1]:
                    for j in range(element_dict['dihedrals']):
                        dihedrals_value.append(data[0][dihedrals_index + 2 + j])
                else:
                    pass
    return pd.DataFrame(dihedrals_value)   

def Save_Torsions_data(element_dict, data):
    torsions_value = []
    for i in range(data.index.stop):
        value = data[0][i]
        if element_dict['torsions'] != 0:
            if 'of torsions' in value:
                torsions_index = i
                if 'V4' in data[0][torsions_index + 1]:
                    for j in range(element_dict['torsions']):
                        pass
                else:
                    pass
    return pd.DataFrame(torsions_value)   
    
def Save_improper_data(element_dict, data):
    improper_value = []
    for i in range(data.index.stop):
        value = data[0][i]
        if element_dict['improper'] != 0:
            if '# improper' in value:
                improper_index = i
                for j in range(element_dict['improper']):
                    improper_value.append(data[0][improper_index + j])
    return pd.DataFrame(improper_value)  

def Atoms_Style(data):
    atoms_style = []
    for i in data[0]:
        atoms_style.append(i.split()[0])
    return set(atoms_style)

def Bonds_Style(data):
    bonds_style = []
    for i in data[0]:
        bonds_style.append(i.split()[-2])
    return set(bonds_style)
    
def Angles_Style(data):
    angles_style = []
    for i in data[0]:
        angles_style.append(i.split()[-2])
    return set(angles_style)    
    
def Dihedrals_Style(data):
    dihedrals_style = []
    for i in data[0]:
        dihedrals_style.append(i.split()[-2])
    return set(dihedrals_style)
    
def Dihedrals_Style(data):
    dihedrals_style = []
    for i in data[0]:
        dihedrals_style.append(i.split()[-2])
    return set(dihedrals_style)

def Torsions_Style(data):
    #待定
    torsions_style = []
    # for i in data[0]:
    #     torsions_style.append(i.split()[-2])
    return set(torsions_style)

def Improper_Style(data):
    improper_style = []
    for i in data[0]:
        improper_style.append(i.split()[-2])
    return set(improper_style)
    
    
