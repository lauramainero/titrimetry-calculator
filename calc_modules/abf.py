"""
Módulo que contém a função para realizar cálculos para a técnica de titulação com ácido fraco e base forte
"""
#TODO: Finalizar a refatoração do código

import math
from time import sleep
from main_modules.again import calculate_again
from main_modules.tabulate import tab1, tab2, tab3
from main_modules.decoration import decoration_line
from main_modules.variables import *

def calculate(mm_ana, v_ana, mm_tit, v_tit_add, eq_point, ka):
    """
    Função que irá realizar os cálculos de ácido fraco com base forte
    """

    global chosen_tec, v_tit_add_list, ph_list

    chosen_tec = 'abf'

    if v_tit_add == 0:
        pka = math.log10(ka) * -1
        print(f'\npKa = -log {ka:.0e} = {pka:.4f}\nO valor do pKa é {pka:.4f}.')

        mm_ka = ka * mm_ana
        n_mm_ana = math.sqrt(mm_ka)
        ph = math.log10(n_mm_ana) * -1
        print('\nHA + H2O \u21CB  H3O+ + A- \nKa = ([H3O+] * [A-]) / [HA]\n[H3O+] = [A-] = [H3O+]\u00b2') # onde HA = ácido fraco e A- dissociação do ácido fraco

        print(f'\n{ka:.0e} = ([H3O+] * [A-]) / {mm_ana}\n[H3O+]\u00b2 = {ka:.0e} * {mm_ana} = {mm_ka:.4e}\n[H3O+] = \u221A{mm_ka:.4e} = {ph:.2f}\nO pH da solução com 0 mL de titulante adicionado é {ph:.2f}.')

    elif v_tit_add < eq_point:
        print("\nHA + OH- \u21CB  A- + H2O") 

        n_mol_ana = mm_ana * (v_ana / 1000)
        print(f'\nnº de íons H3O+ = {mm_ana} / ({v_ana:.4f} / 1000) = {n_mol_ana:.4f}\nO número de mols do analito é {n_mol_ana:.4f}.')

        n_mol_tam = mm_tit * (v_tit_add / 1000)
        print(f'\nnº de mols do tampão = {mm_tit} * ({v_tit_add} / 1000) = {n_mol_tam:.4f}\nO número de mols do tampão formado é {n_mol_tam:.4f}.')

        n_mol_ana_ex = n_mol_ana - n_mol_tam
        print(f'\nnº de mols dos íons H3O+ excedentes = {n_mol_ana:.4f} - {n_mol_tam:.4f} = {n_mol_ana_ex:.4f}\nO número de mols do analito excedente (não reagiu com o titulante) é {n_mol_ana_ex:.4f}.')

        n_mm_tam = n_mol_tam / (v_ana / 1000 + v_tit_add / 1000)
        n_mm_ana = n_mol_ana_ex / (v_ana / 1000 + v_tit_add / 1000)
        print(f'\nMassa molar do tampão = {n_mol_tam:.4f} / ({v_ana / 1000} + {v_tit_add / 1000}) = {n_mm_tam:.4e} mol/L\nNova massa molar do analito = {n_mol_ana_ex:.4f} / ({v_ana / 1000} + {v_tit_add / 1000}) = {n_mol_ana:.4e} mol/L')

        pka = math.log10(ka) * -1

        print(f'\npKa = -log {ka:.0} = {pka:.4f}\nO valor do pKa é {pka:.4f}.')

        ph = pka + math.log10(n_mm_tam / n_mm_ana)

        print(f'\npH = {pka:.4f} + log {n_mm_tam:.3e} / {n_mm_ana:.3e} = {ph:.4f}\nO pH da solução com {v_tit_add:.2f} mL de titulante adicionado é {ph:.4f}.')

        # tab#()

        decoration_line()

        ph_list.append(ph)
    
    elif v_tit_add == eq_point:
        # passo a passo do cálculo para achar o pKa
        pka = math.log10(ka) * -1
        print(f'\npKa = -log {ka:.0e} = {pka:.4f}\nO valor do pKa é {pka:.4f}')

        global KW
        kb = KW / ka
        print(f'\nKa * Kb = Kw\nKb = Kw / Ka\nKb = {KW:.3e} / {ka:.3e} = {kb:.3e}\nO valor do Kb é {kb:.3e}')
    
        n_mol_tam = mm_tit * (v_tit_add / 1000)
        print(f'\nnº mol H3O+ = {mm_tit:.4f} * ({v_tit_add} / 1000) = {n_mol_tam:.4f}\nO número de mols do analito é {n_mm_tam:.4f}.')

        n_mm_tam = n_mol_tam / (v_ana / 1000 + v_tit_add / 1000)
        print(f'\nMassa molar do tampão = {n_mol_tam:.4f} / ({v_ana / 1000} + {v_tit_add / 1000}) = {n_mm_tam:.4e}')

        print('\nKb = ([HA] * [OH-]) / [A-]\nOn the equivalence point, [HA] = [OH-]\nKb = [OH-]\u00b2 / [A-]\n[OH-]\u00b2 = [A-] * Kb')

        kb_mm = n_mm_tam * kb
        n_mm_ana = n_mm_tam # como [HA] = [A-], pode ser feita a equivalência com a molaridade do analito
        n_mm_ana = math.sqrt(kb_mm) 
        poh = math.log10(n_mm_ana) * -1

        print(f'\n[OH-]\u00b2 = {n_mm_tam:.3e} * {kb:.3e} = {kb_mm:.4e}\n[OH-] = \u221A{kb_mm:.4e} = {n_mm_ana:.4f} ')

        print(f'\npOH = -log [OH-]\npOH = -log {n_mm_ana:.4e} = {poh:.4f}')

        print(f'\nO pOH da solução com {v_tit_add:.2f} mL de titulante adicionado é {poh:.4f}.')
    
        print('\npH + pOH = 14\npH = 14 - pOH')

        ph = 14 - poh
        print(f'\npH = 14 - {poh:.4f} = {ph:.4f}\nO pH da solução com {v_tit_add:.2f} mL de titulante adicionado é {ph:.4f}.')

        # tab#()

        decoration_line()

        ph_list.append(ph)

    elif v_tit_add > eq_point:
        n_mol_ana = mm_ana * (v_ana / 1000)
        print(f'\nnº mol H3O+ = {mm_ana:.4f} * ({v_ana:.4f} / 1000) = {n_mol_ana:.4f}\nO número de mols do analito é {n_mol_ana:.4f}.')

        n_mol_tit = mm_tit * (v_tit_add / 1000)
        print(f'\nnº mol OH- = {mm_tit:.4f} * ({v_tit_add:.4f} / 1000) = {n_mol_tit:.4f}\nO número de mols do titulante é {n_mol_tit:.4f}')

        n_mol_analyte_ex = n_mol_tit - n_mol_ana
        print(f'\nnº mol H3O+ restante = {n_mol_tit:.4f} - {n_mol_ana:.4f} = {n_mol_analyte_ex:.4f}\nO número de mols do excesso de titulante é {n_mol_analyte_ex:.4f}.')
    
        titrant_nmm = n_mol_analyte_ex / (v_ana / 1000 + v_tit_add / 1000)
        print(f'\nMM do excesso de titulante = {n_mol_analyte_ex:.4f} / ({v_ana:.4f} + {v_tit_add:.4f}) = {titrant_nmm:.4f}\n\nA massa molar do excesso de titulante é de {titrant_nmm:.4f} mol/L.')
    
        poh = math.log10(titrant_nmm) * -1
        print(f'\npOH = -log {titrant_nmm:.4f} = {poh:.4f}\nO pOH da solução com {v_tit_add:.2f} mL de titulante adicionado é {poh:.4f}.')

        print('\npH + pOH = 14\npH = 14 - pOH')

        ph = 14 - poh
        print(f'\npH = 14 - {poh:.4f} = {ph:.4f}\n\nO pH da solução com {v_tit_add:.2f} mL de titulante adicionado é {ph:.4f}.')

    else:
        print('Por favor, insira valores válidos para a massa molar e o volume')