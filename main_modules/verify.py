"""
Módulo contendo a(s) seguinte(s) função(ões):
- verify_input_value
"""

from main_modules.treatment import function_error_treatment

@function_error_treatment
def verify_input_value(msg, predicate = lambda value: value <= 0):
    """
    Função que recebe valores e verifica se estão nos conformes de cada tipo de dado; utilizada para os valores de titulante adicionado e dados básicos.
    """

    valor = 0
    while True:
        x = float(input(msg))
        if predicate(x):
            print('ERRO: Valor abaixo ou igual a 0. Por favor, revise os valores indicados e tente novamente.')
            continue

        valor = x
        break
    return valor
