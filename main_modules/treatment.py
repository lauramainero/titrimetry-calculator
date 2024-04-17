"""
Módulo contendo a(s) seguinte(s) função(ões):
- function_error_treatment
"""

def function_error_treatment(funcao):
    """
    Função reservada para receber valores de quaisquer funções e tratar seus possíveis erros de entrada.
    """

    def wrapper(*args, **kwargs):
        try:
            resultado = funcao(*args, **kwargs)
            return resultado
        except ValueError:
            print('ERRO: Valores inválidos! Por favor, revise as informações digitadas e insira novos valores.')
            funcao()
        except Exception as erro:
            print(f'ERRO: {erro}!')
    return wrapper