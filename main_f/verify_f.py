# função para receber valores e verificar se estão nos conformes (acima de 0)

def verify(msg):
    try:
        ok = False
        valor = 0
        while True:
            x = float(input(msg))
            if x <= 0:
                print('ERRO: Valor abaixo ou igual a 0. Por favor, revise os valores indicados e tente novamente.')
                continue
            elif x > 0:
                valor = x
                ok = True
            
            if ok:
                break
    except ValueError:
        print('ERRO: Tipo de valor não correspondente. Por favor, reinicie o programa e utilize apenas valores numéricos.')
    return valor
