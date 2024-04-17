"""
Módulo contendo a(s) seguinte(s) função(ões):
- bye_user
"""

from main_modules.decoration import decoration_line

def bye_user():
    """
    Função que imprimirá uma mensagem de despedida ao usuário;
    """
    
    decoration_line()
    
    print(f'''
{"*" * 56}
Obrigado por utilizar a calculadora de titulometria :)
Até os próximos cálculos!
{"*" * 56}
''')
    