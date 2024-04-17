"""
Módulo contendo a(s) seguinte(s) função(ões):
- change_technique_type
"""

from main_modules.tec_selection import tec_selection
from main_modules.verify import verify_input_value
from calc_modules import abf, cpx, ntr, rdx
from main_modules.variables import *

def change_technique_type(chosen_tec):
    """
    Recebe do usuário se ele deseja continuar os cálculos com a técnica utilizada anteriormente ou se prefere trocar a técnica;
    Entrada(s): um caractere S ou N;
    """

    chg_type = input(
        '\nDeseja utilizar a mesma técnica?\nDigite S para sim e N para não.\n''').lower()

    match chg_type:
        case 's':
            v_tit_add = verify_input_value('\nInsira o volume de titulante utilizado (mL): ')
            match chosen_tec: # chama a função correspondente à técnica de cálculos escolhida; lembrando: x = tec
                case 'ntr':
                    ntr.calculate(v_tit_add, eq_point, mm_ana, v_ana, mm_tit)
                case 'abf':
                    # abf.calculate()
                    pass
                case 'cpx':
                    # cpx.calculate()
                    pass
                case 'rdx':
                    # rdx.calculate()
                    pass
        case 'n':
            v_tit_add_list.clear()  # limpa os valores de titulante adicionado da lista
            ph_list.clear()  # limpa os valores de ph da lista
            tec_selection()  # chama a função de início, onde é escolhida a técnica utilizada
        case _:
            print('Por favor, insira um dos caracteres válidos (S ou N).')
            change_technique_type()