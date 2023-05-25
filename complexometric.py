import math

# na volumetria de complexação o titulante é o EDTA, e o titulado é o centro metálico do complexo. O EDTA é um ácido com quatro hidrogênios ionizáveis.

def welcome():
    # saudações ao usuário
    print("\nHello, welcome to the redox titrimetry calculator!")
welcome()

def information():
    # o usuário deverá disponibilizar o MM do titulante, MM do analito e V do analito, além do Ka
    global analyte_mm
    global analyte_v
    global titrant_mm

    analyte_mm = float(input('\nPlease, enter the analyte molarity (mol/L): '))
    analyte_v = float(input('Please, enter the analyte volume (mL): '))
    titrant_mm = float(input('Please, enter the titrant molarity (mol/L): '))

    # o usuário receberá, então, o cálculo do ponto de equivalência
    # passo a passo do cálculo para achar o ponto de equivalência
    global eq_point
    eq_point = (analyte_mm * analyte_v) / titrant_mm
    print("\nC1V1 = C2V2")
    print("V2 = (C1V1)/C2")
    print("\nV2 = " + '({} * {}) / {}'.format(analyte_mm, analyte_v, titrant_mm))
    print("V2 = " + f'{eq_point:.2f}')
    print("\nThe required volume of titrant to reach the equivalence point is " + f'{eq_point:.2f}' + " mL.")

    # o usuário deverá disponibilizar também o pH da solução, bem como o Kabs dado na questão
    global ph
    global kabs

    ph = float(input('\nPlease, enter the pH of the solution: '))
    kabs = float(eval(input('\nPlease, enter the Kabs of the solution: ')))

    # outras variáveis que serão utilizadas
    global k1
    global k2
    global k3
    global k4

    k1 = 1*10**-2
    k2 = 2.2*10**-3
    k3 = 6.9*10**-7
    k4 = 5.5*10**-11
information()

def titrant():
    #o usuário deverá disponibilizar, então, o mL de titulante que foi adicionado
    global titrant_v_used
    titrant_v_used = float(input('\nPlease, enter the used volume of titrant (mL): '))
titrant()

def calculate():
    # serão feitos os cálculos a partir do volume de titulante inserido em relação ao volume do ponto de equivalência
    # como não há EDTA, a concentração de analito livre é a concentração dada
    if titrant_v_used == 0:
        
        p_analyte = math.log10(analyte_mm) * -1
        print("Analyte molarity = " + '{}'.format(analyte_mm))
        print("")
        print("The free molarity of the analyte is " + f'{p_analyte}' + ".")
        

    elif titrant_v_used < eq_point:
         # primeiramente, é calculado o nº de mols do analito 
        n_mol_analyte = analyte_mm * (analyte_v / 1000)
        print("\nnº mol H3O+ = " + '{:.4f} * ({} / 1000) = '.format(analyte_mm, analyte_v) + f'{n_mol_analyte:.4f}')
        print("The mol number of the analyte is " + f'{n_mol_analyte:.4f}' + ".")

        # em seguida, calcula-se o nº de mols de EDTA adicionado
        n_mol_titrant = titrant_mm * (titrant_v_used / 1000)
        print("\nnº mol titrant = " + '{} * ({} / 1000) = '.format(titrant_mm, titrant_v_used) + f'{n_mol_titrant:.4f}')
        print("The mol number of the titrant volume used is " + f'{n_mol_titrant:.4f}' + ".")

        # agora, calcula-se o número de mols do analito livre restante na solução
        n_mol_analyte_dr = n_mol_analyte - n_mol_titrant
        print("\nnº mol analyte left = " + '{:.4f} - {} = '.format(n_mol_analyte, n_mol_titrant) + f'{n_mol_analyte_dr:.4f}')
        print("The mol number of the analyte amount that don't reacted with the titrant is " + f'{n_mol_analyte_dr:.4f}' + ".")
    
        # com o número de mols, encontra-se a nova concentração utilizando tambem o novo volume total
        analyte_nmm = n_mol_analyte_dr / (analyte_v / 1000 + titrant_v_used / 1000)
        print("\nNew analyte molarity = " + '{:.4f} / ({} + {}) = '.format(n_mol_analyte_dr, analyte_v, titrant_v_used) + f'{analyte_nmm:.2e}')
        print("The new molarity of the analyte is " + f'{analyte_nmm:.2e}' + " mol/L.")
    
        # com a concentração, é possível achar o pAnalito
        p_analyte = math.log10(analyte_nmm) * -1
        print("\nPotential = " + '-log {:.2e} = '.format(analyte_nmm) + f'{p_analyte:.2f}')
        print("\nThe solution's analyte potential with " + f'{titrant_v_used:.2f}' + " mL of titrant added is " + f'{p_analyte:.2f}' + ".")

    elif titrant_v_used == eq_point:
        h3o = 10**(-1 * ph)
        print('\npH = -log {:.2e}'.format(h3o))
        print("The solution's [H+] with " + '{:.2e}'.format(h3o) + "mol/L.")
        
        a4 = (k1*k2*k3*k4)/(h3o**4+k1*h3o**3+k1*k2*h3o**2+k1*k2*k3*h3o+k1*k2*k3*k4)
        print("\nK1K2K3K4/[H+]4 + K1[H+]3 + K1K2[H+]2 + K1K2K3[H+] + K1K2K3K4")
        print('({} * {} * {} * {})/{}**4 + {} * {}**3 + {} * {} * {}**2 + {} * {} * {} * {}**1 + {} * {} * {} * {}'.format(k1, k2, k3, k4, h3o, k1, h3o, k1, k2, h3o, k1, k2, k3, h3o, k1, k2, k3, k4) + f'{a4:.3f}')
        print("The solution's \u03B14 is " + f'{a4:.3f}')

        k_linha = kabs * a4
        print("K' = Kabs * \u03B14")
        print("\nK' = " + '{} * a4 = ' + f'{k_linha:.2e}')
        print("The solution's K' is " + f'{k_linha:.2e}')

    # elif titrant_v_used > eq_point:

    # else:

    def again():
        calc_again = input('''
        Do you want to calculate again?
        Please, type Y for yes or N for no.
        ''')

        if calc_again.upper() == 'Y':
            titrant()
            calculate()

        elif calc_again.upper() == 'N':
            print("\nThank you for using the titrimetry calculator, see you later!")

        else:
            again()
    again()
calculate()