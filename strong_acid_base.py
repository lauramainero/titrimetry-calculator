import math 

def welcome():
    # saudações ao usuário
    print("\nHello, welcome to the strong acid-base titrimetry calculator!")
welcome()

def information():
    # o usuário deverá disponibilizar o MM do titulante, MM do analito e V do analito
    global analyte_mm
    global analyte_v
    global titrant_mm

    analyte_mm = float(input('\nPlease, enter the analyte molarity (mol/L): '))
    analyte_v = float(input('Please, enter the analyte volume (mL): '))
    titrant_mm = float(input('Please, enter the titrant molarity (mol/L): '))

    # o usuário receberá, então, o cálculo do ponto de equivalência
    global eq_point
    
    eq_point = (analyte_mm * analyte_v) / titrant_mm

    # passo a passo do cálculo realizado
    print("\nC1V1 = C2V2")
    print("V2 = (C1V1)/C2")
    print("\nV2 = " + '({} . {}) / {}'.format(analyte_mm, analyte_v, titrant_mm))
    print("V2 = " + f'{eq_point:.2f}')
    print("\nThe required volume of titrant to reach the equivalence point is " + f'{eq_point:.2f}' + " mL.")
information()

def titrant():
    # o usuário deverá disponibilizar, então, o mL de titulante que foi adicionado

    global titrant_v_used
    titrant_v_used = float(input('\nPlease, enter the used volume of titrant (mL): '))

titrant()

def calculate():
    # serão feitos os cálculos a partir do volume de titulante inserido em relação ao volume do ponto de equivalência

    if titrant_v_used == 0:
        ph = math.log10(analyte_mm) * -1
        # passo a passo do cálculo de pH
        print("\npH = " + '-log {} = '.format(analyte_mm) + f'{ph:.2f}')
        print("\nThe solution's pH with 0 mL of titrant added is " + f'{ph:.2f}')

    # o pH é calculado em função da concentração de H3O+ proveniente do ácido que não reagiu com a base
    elif titrant_v_used < eq_point:
    
        # primeiramente, é calculado o nº de mols do analito (H3O+)
        n_mol_analyte = analyte_mm * (analyte_v / 1000)
        print("\nnº mol H3O+ = " + '{:.4f} * ({} / 1000) = '.format(analyte_mm, analyte_v) + f'{n_mol_analyte:.4f}')
        print("The mol number of the analyte is " + f'{n_mol_analyte:.4f}' + ".")

        # em seguida, calcula-se o nº de mols do titulante adicionado (OH-)
        n_mol_titrant = titrant_mm * (titrant_v_used / 1000)
        print("\nnº mol OH- = " + '{} * ({} / 1000) = '.format(titrant_mm, titrant_v_used) + f'{n_mol_titrant:.4f}')
        print("The mol number of the titrant volume used is " + f'{n_mol_titrant:.4f}' + ".")

        # agora, calcula-se o número de mols de H3O+ livre restante no analito
        n_mol_analyte_dr = n_mol_analyte - n_mol_titrant
        print("\nnº mol H3O+ left = " + '{:.4f} - {} = '.format(n_mol_analyte, n_mol_titrant) + f'{n_mol_analyte_dr:.4f}')
        print("The mol number of the analyte amount that don't reacted with the titrant is " + f'{n_mol_analyte_dr:.4f}' + ".")
    
        # com o número de mols, encontra-se a nova concentração utilizando tambem o novo volume total
        analyte_nmm = n_mol_analyte_dr / (analyte_v / 1000 + titrant_v_used / 1000)
        print("\nNew H3O+ molarity = " + '{} / ({} + {}) = '.format(f'{n_mol_analyte_dr:.4f}', analyte_v, titrant_v_used) + f'{analyte_nmm:.4f}')
        print("The new molarity of the analyte is " + f'{analyte_nmm:.4f}' + " mol/L.")
    
        # com a concentração, é possível achar o pH com adição de 10 mL de ácido
        ph = math.log10(analyte_nmm) * -1
        print("\npH = " + '-log {:.4} = '.format(analyte_nmm) + f'{ph:.4f}')
        print("\nThe solution's pH with " + f'{titrant_v_used:.2f}' + " mL of titrant added is " + f'{ph:.4f}' + ".")

    # o pH é calculado em função do equilíbrio de H2O
    elif titrant_v_used == eq_point:
    
        # primeiramente, é calculado o nº de mols do analito (H3O+)
        n_mol_analyte = analyte_mm * (analyte_v / 1000)
        print("\nnº mol H3O+ = " + '{} * ({} / 1000) = '.format(analyte_mm, analyte_v) + f'{n_mol_analyte:.4f}')
        print("The mol number of the analyte is " + f'{n_mol_analyte:.4f}')
    
        # como o mL adicionado e as molaridades são as mesmas, temos que nº mol H3O+ = º mol OH-
        print("\n2 H2O \u21CB H3O+ + OH-")
        print("H3O+ = OH- = 1 * 10e-7")

        # portanto, a nova molaridade será dada através do equilíbrio iônico da água, que é 10e-7 tanto para o H3O+ quanto para o OH-
        kw = 1*10**-7
        ph = math.log10(kw) * -1
        print("\npH = " + '-log {} = '.format('1 * 10e-7') + f'{ph:.3f}')
        print("\nThe solution's pH on the equivalence point is " + f'{ph:.3f}' + ".")

    # como já não há mais ácido para reagir, o pH é calculado em função do pOH, a concentração de OH- proveniente do excesso adicionado
    elif titrant_v_used > eq_point:

        # primeiramente, é calculado o nº de mols do analito (H3O+)
        n_mol_analyte = analyte_mm * (analyte_v / 1000)
        print("\nnº mol H3O+ = " + '{:.4f} * ({:.4f} / 1000) = '.format(analyte_mm, analyte_v) + f'{n_mol_analyte:.4f}')
        print("The mol number of the analyte is " + f'{n_mol_analyte:.4f}' + ".")

        # em seguida, calcula-se o nº de mols do titulante (OH-)
        n_mol_titrant = titrant_mm * (titrant_v_used / 1000)
        print("\nnº mol OH- = " + '{} * ({} / 1000) = '.format(f'{titrant_mm:.4f}', f'{titrant_v_used:.4f}') + f'{n_mol_titrant:.4f}')
        print("The mol number of the titrant volume used is " + f'{n_mol_titrant:.4f}' + ".")

        # agora, calcula-se o número de mols de OH- em excesso no analito
        n_mol_analyte_ex = n_mol_titrant - n_mol_analyte
        print("\nnº mol H3O+ left = " + '{:.4f} - {:.4f} = '.format(n_mol_titrant, n_mol_analyte) + f'{n_mol_analyte_ex:.4f}')
        print("The mol number of the titrant excess amount is " + f'{n_mol_analyte_ex:.4f}' + ".")
    
        # com o número de mols, encontra-se a concentração do excesso de OH- utilizando tambem o novo volume total
        titrant_nmm = n_mol_analyte_ex / (analyte_v / 1000 + titrant_v_used / 1000)
        print("\nMM titrant excess = " + '{:.4f} / ({:.4f} + {:.4f}) = '.format(n_mol_analyte_ex, analyte_v, titrant_v_used) + f'{titrant_nmm:.4f}')
        print("The molarity of the titrant excess amount is " + f'{titrant_nmm:.4f}' + " mol/L.")
    
        # com a concentração, é possível achar o pOH
        poh = math.log10(titrant_nmm) * -1
        print("\npOH = " + '-log {:.4f} = '.format(titrant_nmm) + f'{poh:.4f}')
        print("\nThe solution's pOH with " + str(titrant_v_used) + " mL of titrant added is " + f'{poh:.4f}' + ".")

        # a partir das relações entre pH e pOH, é possível encontrar o valor de pH da solução com adição titulante após o PE
        print("\npH + pOH = 14")
        print("pH = 14 - pOH")

        ph = 14 - poh
        print("\npH = 14 - " + f'{poh:.4f}' + " = " + f'{ph:.4f}')
        print("\nThe solution's pH with " + f'{titrant_v_used:.2f}' + " mL of titrant added is " + f'{ph:.4f}' + ".")

    else:
        print("Please, enter valid values for molarity and volume.")

    # função again() para o usuário calcular novamente
    def again():
        calc_again = input('''
        Do you want to calculate again?
        Please, type Y for yes or N for no.\n
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