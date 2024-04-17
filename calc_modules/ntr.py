"""
Módulo que contém a função para realizar cálculos para a técnica de neutralização (ácido-base fortes)
"""

import math
from time import sleep
from main_modules.again import calculate_again
from main_modules.tabulate import tab1, tab2, tab3
from main_modules.decoration import decoration_line
from main_modules.variables import *

def calculate(mm_ana, v_ana, mm_tit, v_tit_add, eq_point):
    """
    Função que irá realizar os cálculos de neutralização
    """

    global chosen_tec, v_tit_add_list, ph_list

    chosen_tec = 'ntr'
    if v_tit_add == 0:
        ph = math.log10(mm_ana) * -1

        print(
            f'\npH = -log{mm_ana} = {ph:.2f}\nO pH da solução com 0 mL de titulante adicionado é {ph:.2f}.')

        decoration_line()

        ph_list.append(ph)  # adiciona o ph calculado à lista de ph
        calculate_again(chosen_tec)

    elif v_tit_add < eq_point:
        n_mol_ana = mm_ana * (v_ana / 1000)

        print(
            f'\nnº de mols do analito = {mm_ana} * ({v_ana} / 1000) = {n_mol_ana:.4f}\nO número de mols do analito é {n_mol_ana:.4f}')

        n_mol_tit = mm_tit * (v_tit_add / 1000)
        sleep(2)

        print(
            f'\nnº de mols do titulante adicionado = {mm_tit:.4f} * ({v_tit_add} / 1000) = {n_mol_tit:.4f}\nO número de mols do titulante adicionado é {n_mol_tit:.4f}.')

        n_mol_ana_ex = n_mol_ana - n_mol_tit
        sleep(2)        


        print(
            f'\nnº mol do analito excedente (não reagiu) = {n_mol_ana:.4f} - {n_mol_tit:.4f} = {n_mol_ana_ex:.4f}\nO número de mols do analito excedente após a reação com o titulante é {n_mol_ana_ex:.4f}.')

        n_mm_ana = n_mol_ana_ex / (v_ana / 1000 + v_tit_add / 1000)
        sleep(2)

        print(
            f'\nNova MM do analito = {n_mol_ana_ex:.4f} / ({v_ana} + {v_tit_add}) = {n_mm_ana:.4f}\nA nova massa molar do analito é de {n_mm_ana:.4f} mol/L.')

        ph = math.log10(n_mm_ana) * -1
        sleep(2)

        print(
            f'\npH = -log{n_mm_ana:.4f} = {ph:.4f}\nO pH da solução com {v_tit_add:.4f} mL de titulante adicionado é {ph:.4f}.')

        sleep(2)
    
        tab1(n_mol_ana, n_mol_tit, n_mol_ana_ex) # cria uma tabela no terminal para ilustrar o passo-a-passo do cálculo

        decoration_line()

        ph_list.append(ph)
        calculate_again(chosen_tec)

    elif v_tit_add == eq_point:
        n_mol_ana = mm_ana * (v_ana / 1000)

        print(f'\nnº mol do analito = {mm_ana:.4f} * ({v_ana} / 1000) = {n_mol_ana:.4f}\nO número de mols do analito é {n_mol_ana:.4f}')
        
        sleep(2)

        print('\n2 H2O \u21CB H3O+ + OH-\nH3O+ = OH- = 1 * 10e-7')

        ph = math.log10(10**-7) * -1
        sleep(2)
        
        print(f'\npH = -log 10e-7 = {ph:.3f}\nO pH da solução em seu ponto de equivalência é {ph:.3f}.')
        
        sleep(2)

        tab2(n_mol_ana)

        decoration_line()

        ph_list.append(ph)
        calculate_again(chosen_tec)

    elif v_tit_add > eq_point:
        n_mol_ana = mm_ana * (v_ana / 1000)
        
        print(f'\nnº mol do analito = {mm_ana:.4f} * ({v_ana} / 1000) = {n_mol_ana:.4f}\nO número de mols do analito é {n_mol_ana:.4f}')
        
        n_mol_tit = mm_tit * (v_tit_add / 1000)
        sleep(2)
        
        print(f'\nnº mol do titulante = {mm_tit:.4f} * ({v_tit_add} / 1000) = {n_mol_tit:.4f}\nO número de mols do titulante adicionado é {n_mol_tit:.4f}.')
        
        n_mol_tit_ex = n_mol_tit - n_mol_ana
        sleep(2)
        
        print(f'\nnº mol do titulante excedente = {n_mol_tit:.4f} - {n_mol_ana:.4f} = {n_mol_tit_ex:.4f}\nO número de mols do titulante excedente após a reação com o analito é {n_mol_tit_ex:.4f}.')
        
        n_mm_tit = n_mol_tit_ex / (v_ana / 1000 + v_tit_add / 1000)
        sleep(2)
        
        print(f'\nNova MM do excesso de titulante = {n_mol_tit_ex:.4f} / ({v_ana} + {v_tit_add}) = {n_mm_tit:.4f}\nA massa molar do excesso de titulante é de {n_mm_tit:.4f} mol/L.')
        
        ph = math.log10(n_mm_tit) * -1
        sleep(2)
        
        print(f'\npH = -log{n_mm_tit:.4f} = {ph:.4f}\nO pH da solução com {v_tit_add:.4f} mL de titulante adicionado é {ph:.4f}.')
        
        sleep(2)

        tab3(n_mol_ana, n_mol_tit, n_mol_tit_ex)

        decoration_line()

        ph_list.append(ph)
        calculate_again(chosen_tec)

        return ph
