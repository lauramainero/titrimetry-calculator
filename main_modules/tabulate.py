"""
Módulo contendo a(s) seguinte(s) função(ões):
- tab1
- tab2
- tab3
"""

# Não há grandes diferenças entre cada tabela, são criadas separadamente apenas para facilitar a inserção dos dados que as compõem; podem ser alteradas futuramente

#TODO: Revisar e refatorar as funções

from tabulate import tabulate

# NTR
## v_tit_add < eq_point
def tab1(a, b, c):
    """
    Função para imprimir a tabela dos cálculos feitos com o volume de titulante abaixo do ponto de equivalência;
    """

    a = '{:.4f}'.format(a)
    b = '{:.4f}'.format(b)
    c = '{:.4f}'.format(c)

    data = {
        'x': ['Início', 'Adicionado', 'Reagiu', 'Final'],
        'Analito': [a, '-', b, c,],
        'Titulante': ['-', b, b, '-'],
        'Espécie formada 1': ['-', '-', b, b],
        'Espécie formada 2': ['-', '-', b, b]
    }

    tab1 = tabulate(data, headers="keys", tablefmt="pretty")
    print("\n",tab1)

## v_tit_add = eq_point
def tab2(a):
    """
    Função para imprimir a tabela dos cálculos feitos com o volume de titulante no ponto de equivalência;
    """

    a = '{:.4f}'.format(a)

    data = {
    'x': ['Início', 'Adicionado', 'Reagiu', 'Final'],
    'Analito': [a, '-', a, '-'],
    'Titulante': ['-', a, a, '-'],
    'Espécie formada 1': ['-', '-', a, a],
    'Espécie formada 2': ['-', '-', a, a]
    }

    tab2 = tabulate(data, headers="keys", tablefmt="pretty") 
    print("\n", tab2)

## v_tit_add > eq_point
def tab3(a, b, c):
    """
    Função para imprimir a tabela dos cálculos feitos com o volume de titulante acima do ponto de equivalência;
    """

    a = '{:.4f}'.format(a)
    b = '{:.4f}'.format(b)
    c = '{:.4f}'.format(c)

    data = {
    'x': ['Início', 'Adicionado', 'Reagiu', 'Final'],
    'Analito': [a, '-', a, '-'],
    'Titulante': ['-', b, a, c],
    'Espécie formada 1': ['-', '-', a, a],
    'Espécie formada 2': ['-', '-', a, a]
    }

    tab3 = tabulate(data, headers="keys", tablefmt="pretty")
    print("\n", tab3)
