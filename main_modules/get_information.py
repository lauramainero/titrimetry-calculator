"""
Módulo contendo a(s) seguinte(s) função(ões):
- getting_info
- matching_technique
- case_neutral
- case_abf
- case_redox
- case_complex
"""

from main_modules.tec_selection import tec_selection
from main_modules.verify import verify_input_value
from main_modules.eq_point import getting_equivalence_point
from main_modules.add_titrant import titrant_volume_added
from main_modules.decoration import decoration_line
from main_modules.variables import *
from calc_modules import abf, cpx, ntr, rdx

def case_neutral():
    """
    Função simples para chamar a função que realiza os cálculos da técnica de neutralização
    """
    ntr.calculate(mm_ana, v_ana, mm_tit, v_tit_add, eq_point)


def case_abf():
    """
    Função para receber informações pontuausi da técnica de titulometria com ácido fraco e base forte e chamar a função que realiza os cálculos;
    Entrada(s): valor do Ka;
    """

    global ka
    
    ka = verify_input_value('Insira o valor do Ka: ')

    abf.calculate(mm_ana, v_ana, mm_tit, v_tit_add, eq_point, ka)


def case_redox():
    """
    Função para receber informações pontuais da técnica de oxirredução e chamar a função que realiza os cálculos;
    Entrada(s): valores dos potenciais de redução do analito e do titulante;
    Saída(s): agente redutor, agente oxidante, novo potencial de redução e reação global;
    """

    rp_ana = verify_input_value('\nInsira o potencial de redução do analito: ')
    rp_tit = verify_input_value('Insira o potencial de redução do titulante: ')

    analito_estado = 'reduzir' if rp_ana > rp_tit else 'oxidar'
    titulante_estado = 'oxidar' if rp_ana > rp_tit else 'reduzir'
    agente_reduziu = 'titulante' if rp_ana > rp_tit else 'analito'
    novo_potencial_reducao = rp_tit * - 1 if agente_reduziu == 'titulante' else rp_ana * -1
    reacao_global = (rp_tit * -1 + rp_ana) if rp_ana > rp_tit else (rp_ana * -1 + rp_tit)

    print(f'\nO analito irá {analito_estado} e o titulante irá {titulante_estado}.\nO novo potencial de redução do {agente_reduziu} é {novo_potencial_reducao}.\nA reação global do potencial de redução é {reacao_global:.2f}.\n')

    if agente_reduziu == 'titulante':
        rp_tit *= -1
    else:
        rp_ana *= -1

    rdx.calculate()


def case_complex():
    """
    Função para receber informações pontuais da técnica de complexação e chamar a função que realiza os cálculos;
    Entrada(s): valor do pH e do Kabs;
    """
    global ph, kabs
    
    ph = verify_input_value('\nInsira o pH da solução: ')
    kabs = verify_input_value('Insira o Kabs da solução: ')

    cpx.calculate()

def matching_technique():
    """
    Função para chamar as funções de cálculo de acordo com a técnica escolhida.
    """

    match chosen_tec:
        case 'ntr':
            case_neutral()
        case 'ABF':
            case_abf()
        case 'CPX':
            case_complex()
        case 'RDX':
            case_redox()

def getting_info():
    """
    Função que recebe as principais informações para realizar cálculos; independem da técnica escolhida;
    """
    global chosen_tec
    chosen_tec = tec_selection()

    print(f'\n{"*" * 18}\nColetando dados...\n{"*" * 18}')

    global mm_ana, v_ana, mm_tit
    mm_ana = verify_input_value('\n▷ Insira a massa molar do analito utilizado (mol/L): ')
    v_ana = verify_input_value('▷ Insira o volume do analito utilizado (mL): ')
    mm_tit = verify_input_value('▷ Insira a massa molar do titulante utilizado (mol/L): ')

    decoration_line()

    global eq_point
    eq_point = getting_equivalence_point(mm_ana, v_ana, mm_tit)

    global v_tit_add
    v_tit_add = titrant_volume_added()

    matching_technique()
