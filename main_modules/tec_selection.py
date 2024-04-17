"""
Módulo contendo a(s) seguinte(s) função(ões):
- tec_selection
"""

from main_modules.decoration import decoration_line

def tec_selection():
    """
    Função que lista as técnicas de titulometria disponíveis e recebe a técnica que o usuário deseja utilizar;
    Entrada(s): uma string com a sigla da técnica desejada;
    """

    global chosen_tec
    
    chosen_tec = input('''
Digite a sigla equivalente à técnica que deseja utilizar nos cálculos:
NTR - Neutralização
ABF - Ácido fraco e Base forte
AFB - Ácido forte e Base fraca (INDISPONÍVEL)
MHR - Método de Mohr (INDISPONÍVEL)
VOL - Método de Volhard (INDISPONÍVEL)
FAJ - Método de Fajans (INDISPONÍVEL)
CPX - Complexação
RDX - Redox (Oxirredução)
                       
▷ RESPOSTA: ''').lower()
    
    while chosen_tec != 'ntr' and chosen_tec != 'abf' and chosen_tec != 'cpx' and chosen_tec != 'rdx':
        print("\nERRO: Digite alguma das siglas das técnicas disponíveis.")
        chosen_tec = input('▷ RESPOSTA: ').lower()

    decoration_line()
    return chosen_tec