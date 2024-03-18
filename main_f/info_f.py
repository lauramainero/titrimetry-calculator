# função para receber valores que serão utilizados de maneira geral, indepentende da técnica utilizada 

def info():
    global mm_ana, v_ana, mm_tit
    mm_ana = verify('\nInsira a massa molar do analito utilizado (mol/L): ')
    v_ana = verify('Insira o volume do analito utilizado (mL): ')
    mm_tit = verify('Insira a massa molar do titulante utilizado (mol/L): ')

    global eq_point
    eq_point = (mm_ana * v_ana) / mm_tit
	
    print(f'''
	C1V1 = C2V2
	V2 = (C1V1)/C2
	V2 = ({mm_ana} . {v_ana}) / {mm_tit}
	V2 = {eq_point:.2f}
	\nO volume de titulante necessário para atingir o ponto de equivalência é de {eq_point:.2f} mL.
    ''')

    match tec:
        case 'NTR':
            titrant()
            calc_ntr()
        case 'ABF':
            global ka # não sei se essas variáveis globais deveriam ser assim declaradas dentro de uma função
            verify(ka, 'Insira o valor do Ka: ')
            titrant()
            calc_abf()
        case 'CPX':
            global ph, kabs 
            verify(ph, 'Insira o pH da solução: ')
            verify(kabs, 'Insira o Kabs da solução: ')
            
            global k1, k2, k3, k4 
            k1, k2, k3, k4 = 1*10**-2, 2.2*10**-3, 6.9*10**-7, 5.5*10**-11
            titrant()
            calc_cpx()
        case 'RDX':
            global rp_ana, rp_tit
            rp_ana = float(input('\nInsira o potencial de redução do analito: '))
            rp_tit = float(input('Insira o potencial de redução do titulante: '))

            if rp_ana > rp_tit:
                print(f'''O analito irá reduzir e o titulante irá oxidar.
                    O novo potencial de redução do titulante é {rp_tit * -1}.
                    A reação global do potencial de redução é {rp_tit * -1 + rp_ana:.2f}.
                    ''')
                rp_tit *= -1
                titrant()
                calc_rdx()

            elif rp_ana < rp_tit:
                print(f'''O analito irá oxidar e o titulante irá reduzir.
                    O novo potencial de redução do analito é {rp_ana * -1}.
                    A reação global do potencial de redução é {rp_ana * -1 + rp_tit:.2f}.
                    ''')
                rp_ana *= -1
                titrant()
                calc_rdx()

            else:
                print("Ocorreu um erro. Por favor, insira valores válidos para os potenciais de redução." )