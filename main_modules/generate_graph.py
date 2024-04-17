"""
Módulo contendo a(s) seguinte(s) função(ões):
- generate_graph
"""

import matplotlib.pyplot as plt

def generate_graph(x, y):
    """
    Cria um gráfico com os dados gerados nos cálculos e armazenados nas listas;
    """

    plt.title('Curva de Titulação')
    plt.xlabel('Volume de titulante (mL)')
    plt.ylabel('pH')

    plt.plot(x, y)
    plt.show()