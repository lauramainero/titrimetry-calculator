def welcome():
    print('''
    \n==================================================
    \nOlá, seja bem-vindo à calculadora de titulometria!
    \n==================================================
    ''')

    tec = input('''
    Digite a sigla equivalente à técnica que deseja utilizar nos cálculos:
    NTR - Neutralização
    ABF - Ácido fraco e Base forte
    AFB - Ácido forte e Base fraca (INDISPONÍVEL)
    MHR - Método de Mohr (INDISPONÍVEL)
    VOL - Método de Volhard (INDISPONÍVEL)
    FAJ - Método de Fajans (INDISPONÍVEL)
    CPX - Complexação
    RDX - Redox (Oxirredução)\n
    ''')
