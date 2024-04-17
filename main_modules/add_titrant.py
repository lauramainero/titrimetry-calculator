"""
Módulo contendo a(s) seguinte(s) função(ões):
- titrant_volume_added
"""

from main_modules.treatment import function_error_treatment
from main_modules.verify import verify_input_value
from main_modules.decoration import decoration_line
from main_modules.variables import *

@function_error_treatment
def titrant_volume_added():
    """
    Função para receber o valor de titulante adicionado;
    Entrada(s): o valor de titulante que o usuário deseja utilizar nos cálculos;
    """

    v_tit_add = verify_input_value('\n▷ Insira o volume de titulante utilizado (mL): ', lambda value: value < 0)

    v_tit_add_list.append(v_tit_add)

    decoration_line()

    return v_tit_add