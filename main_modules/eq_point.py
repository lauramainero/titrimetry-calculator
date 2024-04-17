"""
Módulo contendo a(s) seguinte(s) função(ões):
- getting_equivalence_point
"""

from main_modules.decoration import decoration_line

def getting_equivalence_point(mm_ana, v_ana, mm_tit):
    """
    Função que calcula o ponto de equivalência da titulação dados a massa molar e o volume do analito e a massa molar do titulante;
    """


    eq_point = (mm_ana * v_ana) / mm_tit

    print(f'\nC1V1 = C2V2\nV2 = (C1V1)/C2\nV2 = ({mm_ana} . {v_ana}) / {mm_tit}\nV2 = {eq_point:.2f}\nO volume de titulante necessário para atingir o ponto de equivalência é de {eq_point:.2f} mL.')
    
    decoration_line()

    return eq_point
