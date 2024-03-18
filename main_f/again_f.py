v_tit_add_lis, ph_lis = [], [] # lista de dados que vou usar pra construção dos gráficos; não sei se deveriam ser declaradas aqui mesmo

def again(x): # x = tec, a técnica de titulometria utilizada
    calc_again = input('''
    Deseja realizar outro cálculo?
    Digite S para sim e N para não.\n
    ''')

    if calc_again.upper() == 'S':
        chg_type = input('''
        Deseja utilizar a mesma técnica?
        Digite S para sim e N para não.\n
        ''')

        if chg_type.upper() == 'S':
            v_tit_add = titrant('\nInsira o volume de titulante utilizado (mL): ')
            match x: # chama a função correspondente à técnica de cálculos escolhida; lembrando: x = tec
                case 'NTR':
                    calc_ntr()
                case 'ABF':
                    calc_abf()
                case 'CPX':
                    calc_cpx()
                case 'RDX':
                    calc_rdx()

        elif chg_type.upper() == 'N':
            v_tit_add_lis.clear() # limpa os valores de titulante adicionado da lista
            ph_lis.clear() # limpa os valores de ph da lista
            welcome() # chama a função de início, onde é escolhida a técnica utilizada

        elif chg_type.upper != 'S' and chg_type.upper != 'N':
            print('Por favor, insira um dos caracteres válidos (S ou N).')

        else:
            again()

    elif calc_again.upper() == 'N':
        print('''
        ================================================
        Obrigado por usar a calculadora de titulometria!
        ================================================
        ''')
        graph = input('''
        Deseja formar um gráfico com seus resultados?
        Digite S para sim e N para não.\n
        ''')

        if graph.upper() == 'S':
            graph(v_tit_add_lis, ph_lis) # chama a função que formará o gráfico com os dados das listas

        elif graph.upper() == 'N':
            v_tit_add_lis.clear() # limpa os valores de titulante adicionado da lista
            ph_lis.clear() # limpa os valores do ph da lista
            print('''
            =========================
            Até os próximos cálculos!
            =========================
            ''')

        else:
            print('Por favor, insira um dos caracteres válidos (S ou N).')

    elif calc_again.upper() != 'S' and calc_again().upper != 'N':
        print('Por favor, insira um dos caracteres válidos (S ou N).')

    else:
        again()
