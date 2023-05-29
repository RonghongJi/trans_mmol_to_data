import pandas as pd
import numpy as np
import time
from Data_Processing import *

def Header_to_data(f, element_dict, styl_dict):
    f.write('Lammps data file\n\n')
    if element_dict['atoms'] != 0:
        f.write('{:14}\t atoms\n'.format(element_dict['atoms']))
    if element_dict['bonds'] != 0:
        f.write('{:14}\t bonds\n'.format(element_dict['bonds']))
    if element_dict['angles'] != 0:
        f.write('{:14}\t angles\n'.format(element_dict['angles']))
    if element_dict['torsions'] != 0:
        f.write('{:14}\t torsions\n'.format(element_dict['torsions']))
    if element_dict['dihedrals'] != 0:
        f.write('{:14}\t dihedrals\n'.format(element_dict['dihedrals']))
    if element_dict['improper'] != 0:
        f.write('{:14}\t\timproper\n'.format(element_dict['improper']))
    f.write('\n')
    
    if element_dict['atoms'] != 0:
        f.write('{:14}\t atom types\n'.format(styl_dict['atoms_style']))
    if element_dict['bonds'] != 0:
        f.write('{:14}\t bond types\n'.format(styl_dict['bonds_style']))
    if element_dict['angles'] != 0:
        f.write('{:14}\t angle types\n'.format(styl_dict['angles_style']))
    if element_dict['torsions'] != 0:
        f.write('{:14}\t torsions types\n'.format(styl_dict['torsions_style']))
    if element_dict['dihedrals'] != 0:
        f.write('{:14}\t dihedrals types\n'.format(styl_dict['dihedrals_style']))
    if element_dict['improper'] != 0:
        f.write('{:14}\t\timproper types\n'.format(styl_dict['improper_style']))
    f.write('\n')   
    f.write('xxxxxxxxxxxxxxxxxx\n')
    f.write('xxxxxxxxxxxxxxxxxx\n')
    f.write('xxxxxxxxxxxxxxxxxx\n')
    f.write('\n')
    
def Masses_to_data(file, data_dict):
    file.write('Masses\n\n')
    for i, value in enumerate(data_dict['Atoms_data'][0]):
        file.write('{:8} {:2.6f} {}\n'.format(i + 1, float(value.split()[4]), '#' + value.split()[0]))
    file.write('\n')
    
def PairCoeffs_to_data(file, data_dict):
    file.write('Pair Coeffs\n\n')
    for i, value in enumerate(data_dict['Atoms_data'][0]):
        file.write('{:8} {:2.6f}    {:2.6f} {}\n'.format(i + 1, float(value.split()[-3]), float(value.split()[-4]), '#' + value.split()[0]))
    file.write('\n')    
    
    
def BondCoeffs_to_data(file, data_dict):
    file.write('Bond Coeffs\n\n')
    for i, value in enumerate(data_dict['Bonds_data'][0]):
        file.write('{:8} {:2.6f}    {:2.6f} {}\n'.format(i + 1, float(value.split()[-4]), float(value.split()[3]), '#' + value.split()[-2].split('-')[0] + '  ' + value.split()[-2].split('-')[1]))
    file.write('\n')    
    
def AngleCoeffs_to_data(file, data_dict):
    file.write('Angle Coeffs\n\n')
    for i, value in enumerate(data_dict['Angles_data'][0]):
        file.write('{:8} {:2.6f}    {:2.6f} {}\n'.format(i + 1, float(value.split()[4]), float(value.split()[3]), value.split()[-2].replace('-', '   ')))
    file.write('\n')    
    
def DihedralCoeffs_to_data(file, data_dict):
    file.write('Dihedral Coeffs\n\n')
    for i, value in enumerate(data_dict['Dihedrals_data'][0]):
        file.write('{:8} {:2.6f}    {:2.6f}    {:2.6f}    {:2.6f} {}\n'.format(i + 1, float(value.split()[4]), float(value.split()[5]), float(value.split()[6]), float(value.split()[7]), value.split()[-2].replace('-', '   ')))
    file.write('\n')    
    
def Atoms_to_data(file, data_dict):
    atoms_style_list = list(Atoms_Style(data_dict['Atoms_data']))
    file.write('Atoms\n\n')
    for i, value in enumerate(data_dict['Atoms_data'][0]):
        file.write('{:8} {:8} {:8} {:.5f} {:.5f} {:.5f} {:.5f} {}\n'.format(  i + 1
                                                                             ,1
                                                                             ,atoms_style_list.index(value.split()[0])
                                                                             ,float(value.split()[-4])
                                                                             ,float(value.split()[1])
                                                                             ,float(value.split()[2])
                                                                             ,float(value.split()[3])
                                                                             ,'#' + value.split()[0]))
    file.write('\n')    
    
def Velocities_to_data(file, data_dict):
    file.write('Velocities\n\n')
    for i, value in enumerate(data_dict['Atoms_data'][0]):
        file.write('{:8} {:.5f} {:.5f} {:.5f} {}\n'.format(i + 1 
                                                          ,0
                                                          ,0
                                                          ,0
                                                          ,'#' + value.split()[0]))
    file.write('\n')    

def Bonds_to_data(file, data_dict):
    bonds_style_list = list(Bonds_Style(data_dict['Bonds_data']))
    file.write('Bonds\n\n')
    for i, value in enumerate(data_dict['Bonds_data'][0]):
        file.write('{:8} {:8} {:8} {:8} {}\n'.format(i + 1 
                                                    ,bonds_style_list.index(value.split()[-2])
                                                    ,value.split()[1]
                                                    ,value.split()[2]
                                                    ,'#' + value.split()[-2].split('-')[0] + '    - ' +value.split()[-2].split('-')[1]))
    file.write('\n')    


def Angles_to_data(file, data_dict):
    angles_style_list = list(Angles_Style(data_dict['Angles_data']))
    file.write('Angles\n\n')
    for i, value in enumerate(data_dict['Angles_data'][0]):
        file.write('{:8} {:8} {:8} {:8} {:8}\n'.format(i + 1 
                                                      ,angles_style_list.index(value.split()[-2])
                                                      ,int(value.split()[0])
                                                      ,int(value.split()[1])
                                                      ,int(value.split()[2])))
    file.write('\n')   



def Dihedrals_to_data(file, data_dict):
    dihedrals_style_list = list(Angles_Style(data_dict['Dihedrals_data']))
    file.write('Dihedrals\n\n')
    for i, value in enumerate(data_dict['Dihedrals_data'][0]):
        file.write('{:8} {:8} {:8} {:8} {:8} {:8}\n'.format(i + 1 
                                                           ,dihedrals_style_list.index(value.split()[-2])
                                                           ,int(value.split()[0])
                                                           ,int(value.split()[1])
                                                           ,int(value.split()[2])
                                                           ,int(value.split()[3])))
    file.write('\n')    

def to_data(element_dict, styl_dict, data_dict, utputarg):
    file = open(utputarg, 'w+')
    Header_to_data(file, element_dict, styl_dict)
    Masses_to_data(file, data_dict)
    PairCoeffs_to_data(file, data_dict)
    BondCoeffs_to_data(file, data_dict)
    AngleCoeffs_to_data(file, data_dict)
    DihedralCoeffs_to_data(file, data_dict)
    Atoms_to_data(file, data_dict)
    Velocities_to_data(file, data_dict)
    Bonds_to_data(file, data_dict)
    Angles_to_data(file, data_dict)
    Dihedrals_to_data(file, data_dict)
    file.close()


    