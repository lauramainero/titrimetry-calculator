"""
Módulo contendo a(s) seguinte(s) função(ões):
- calculate_again
- wanna_generate_graph
"""

from main_modules.change_technique import change_technique_type
from main_modules.decoration import decoration_line
from main_modules.bye_user import bye_user
from main_modules.variables import *

global calc_again, chg_type, graph

def wanna_generate_graph():
    """
    Função para receber do usuário de ele deseja ou não gerar um gráfico com os valores gerados;
    Entrada(s): um caractere S ou N;
    """

    graph = input('\nDeseja formar um gráfico com seus resultados?\nDigite S para sim e N para não.\n▷ RESPOSTA: ').lower()

    match graph:
        case 's':
            # chama a função que formará o gráfico com os dados das listas
            graph(v_tit_add_list, ph_list)
            bye_user()
        case 'n':
            v_tit_add_list.clear()  # limpa os valores de titulante adicionado da lista
            ph_list.clear()  # limpa os valores do ph da lista
            bye_user()
        case _:
            print('\nPor favor, insira um dos caracteres válidos (S ou N).')
            wanna_generate_graph()


def calculate_again(chosen_tec): # chosen_tec_var = a variável da técnica de titulometria utilizada que é recebida em tec_selection
    """
    Função inicial para reiniciar os cálculos; recebe do usuário de ele deseja calcular novamente ou não;
    Entrada(s): um caractere S ou N;
    """

    calc_again = input('\nDeseja realizar outro cálculo?\nDigite S para sim e N para não.\n▷ RESPOSTA: ').lower()

    match calc_again:
        case 's':
            change_technique_type(chosen_tec)
        case 'n':
            wanna_generate_graph()
        case _:
            print('\nPor favor, insira um dos caracteres válidos (S ou N).')
            calculate_again()

