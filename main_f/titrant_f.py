# quase igual a função verify_f; mas recebe e verifica apenas os valores do titulante adicionado (igual ou maior que 0)

def titrant(msg):
    try:
        ok = False
        valor = 0
        while True:
            x = float(input(msg))
            if x < 0:
                print('ERRO: Valor abaixo de 0. Por favor, revise os valores indicados e tente novamente.')
                continue
            elif x >= 0:
                valor = x
                ok = True
            if ok:
                break
    except ValueError:
        print('ERRO: Tipo de valor não correspondente. Por favor, reinicie o programa e utilize apenas valores numéricos.')
    return valor