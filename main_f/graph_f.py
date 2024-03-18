# função para criar o gráfico com os dados gerados nos cálculos e armazenados nas listas

import matplotlib.pyplot as plt

def graph(x, y):
    plt.title('Curva de Titulação')
    plt.xlabel('Volume de titulante (mL)')
    plt.ylabel('pH')

    plt.plot(x, y)
    plt.show()