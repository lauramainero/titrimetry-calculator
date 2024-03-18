# função para criar as tabelas que aparecem no terminal; servem apenas para ilustrar os cálculos

from tabulate import tabulate

# NTR
## v_tit_add == 0

## v_tit_add < eq_point
def tab1(a, b, c):
    data = {
        'x': ['Início', 'Adicionado', 'Reagiu', 'Final'],
        'Analito': [a, '-', b, c,],
        'Titulante': ['-', b, b, '-'],
        'Espécie formada 1': ['-', '-', b, b],
        'Espécie formada 2': ['-', '-', b, b]
    }

    print(tabulate(data, headers="keys", tablefmt="pretty"))

## v_tit_add = eq_point
def tab2(a):
    data = {
    'x': ['Início', 'Adicionado', 'Reagiu', 'Final'],
    'Analito': [a, '-', a, '-'],
    'Titulante': ['-', a, a, '-'],
    'Espécie formada 1': ['-', '-', a, a],
    'Espécie formada 2': ['-', '-', a, a]
    }

    print(tabulate(data, headers="keys", tablefmt="pretty"))

## v_tit_add > eq_point
def tab3(a, b, c):
    data = {
    'x': ['Início', 'Adicionado', 'Reagiu', 'Final'],
    'Analito': [a, '-', a, '-'],
    'Titulante': ['-', b, a, 'c'],
    'Espécie formada 1': ['-', '-', a, a],
    'Espécie formada 2': ['-', '-', a, a]
    }

    print(tabulate(data, headers="keys", tablefmt="pretty"))
