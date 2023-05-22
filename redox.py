import math

# a titulação redox envolve a transferência de elétrons entre o titulante e o analito

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

    # o usuário deverá disponibilizar também os potenciais de redução de cada substância
    global analyte_rp
    global titrant_rp

    analyte_rp = float(input('\nPlease, enter the analyte reduction potential: '))
    titrant_rp = float(input('Please, enter the titrant reduction potential: '))

    if analyte_rp > titrant_rp:
        print("\nThe analyte will reduce and the titrant will oxidize.")
        print("The new reduction potential of the titrant species is " + f'{titrant_rp * -1}' + ".")
        print("The global reaction reduction potential is " + f'{(titrant_rp * -1 + analyte_rp):.2f}' + ".")

    elif analyte_rp < titrant_rp:
        print("\nThe analyte will oxidize and the titrant will reduce.")
        print("The new reduction potential of the analyte species is " + f'{analyte_rp * -1}' + ".")
        print("The global reaction reduction potential is " + f'{(analyte_rp * -1 + titrant_rp):.2f}' + ".")

    else:
        print("Please enter valid values for molarity, volume and reductive potentials" )
information()

def titrant():
    #o usuário deverá disponibilizar, então, o mL de titulante que foi adicionado
    global titrant_v_used
    titrant_v_used = float(input('\nPlease, enter the used volume of titrant (mL): '))
titrant()

def calculate():
    # serão feitos os cálculos a partir do volume de titulante inserido em relação ao volume do ponto de equivalência
    # o potencial não poderá ser calculado, pois não há nenhuma especie sendo oxidada ou reduzida
    if titrant_v_used == 0:
        print("Unable to calculate potential.")

    elif titrant_v_used < eq_point:

        # primeiramente, é calculado o nº de mols do analito
        n_mol_analyte = analyte_mm * (analyte_v / 1000)
        print("\nnº mol analyte = " + '{} * ({} / 1000) = '.format(f'{analyte_mm:.4f}', analyte_v) + f'{n_mol_analyte:.4f}')
        print("The mol number of the analyte is " + f'{n_mol_analyte:.4f}')

        # em seguida, calcula-se o nº de mols do titulante adicionado
        n_mol_titrant = titrant_mm * (titrant_v_used / 1000)
        print("\nnº mol titrant = " + '{} * ({} / 1000) = '.format(titrant_mm, titrant_v_used) + f'{n_mol_titrant:.4f}')
        print("The mol number of the titrant volume used is " + f'{n_mol_titrant:.4f}')
    
        # agora, calcula-se o número de mols de analito que não oxidou/reduziu
        n_mol_analyte_dr = n_mol_analyte - n_mol_titrant
        print("\nnº mol analyte left = " + '{:.4f} - {} = '.format(n_mol_analyte, n_mol_titrant) + f'{n_mol_analyte_dr:.4f}')
        print("The mol number of the analyte amount that don't reacted with the titrant is " + f'{n_mol_analyte_dr:.4f}')

        # em seguida, calcula-se o nº de mols do analito que reagiu, ou seja, oxidou/reduziu
        n_mol_analyte_r = n_mol_analyte - n_mol_analyte_dr
        print("\nnº mol analyte don't reacted = " + '{:.4f} - {:.4f} = '.format(n_mol_analyte, n_mol_analyte_dr) )
        print("The mol number of the tampon is " + f'{n_mol_analyte_r:.4f}')

        # por fim, calcula-se o potencial utilizando a equação de Nerst
        # como essa equação é utilizada na redução, o potencial da espécie que oxida deve ter seu sinal original
        potential = analyte_rp - 0.0592/1 * math.log10(n_mol_analyte_dr/n_mol_analyte_r)
        print('E = Eº - 0.0592/nE * log Q' + ", where Q is the ratio between the non-reacted and the reacted species.")
        print('E = {} - 0.592/1 * log {:.4f}/{:.4f} = '.format(analyte_rp, n_mol_analyte_dr, n_mol_analyte_r) + f'{potential:.2f}')
        print("\nThe solution's potential with " + f'{titrant_v_used:.2f}' + " mL is " + f'{potential:.2f}' + "V.")

    # o potencial será a média ponderada dos potenciais individuais
    elif titrant_v_used == eq_point:
        potential = (analyte_rp + titrant_rp)/2
        print('\nE = (n * Q1 + n * Q2)/n + n')
        print('E = (1 * {} + 1 * {})/1 + 1 = '.format(analyte_rp, titrant_rp) + f'{potential:.2f}')
        print("\nThe solution's potential with " + f'{titrant_v_used:.2f}' + " mL is " + f'{potential:.2f}' + "V.")
        
    # o potencial será calculado com base no potencial 
    elif titrant_v_used > eq_point:

         # primeiramente, é calculado o nº de mols do analito
        n_mol_analyte = analyte_mm * (analyte_v / 1000)
        print("\nnº mol analyte = " + '{} * ({} / 1000) = '.format(f'{analyte_mm:.4f}', analyte_v) + f'{n_mol_analyte:.4f}')
        print("The mol number of the analyte is " + f'{n_mol_analyte:.4f}')

        # em seguida, calcula-se o nº de mols do titulante adicionado
        n_mol_titrant = titrant_mm * (titrant_v_used / 1000)
        print("\nnº mol titrant = " + '{} * ({} / 1000) = '.format(titrant_mm, titrant_v_used) + f'{n_mol_titrant:.5f}')
        print("The mol number of the titrant volume used is " + f'{n_mol_titrant:.4f}')
    
        # em seguida, calcula-se o nº de mols em excesso do titulante
        n_mol_analyte_dr = n_mol_titrant - n_mol_analyte
        print("\nnº mol titrant excess = " + '{:.4f} - {:.5f} = '.format(n_mol_titrant, n_mol_analyte) + f'{n_mol_analyte_dr:.5f}' )
        print("The mol number of the titrant excess is " + f'{n_mol_analyte_dr:.5f}')

        # em seguida, calcula-se o nº de mols do analito que reagiu, ou seja, oxidou/reduziu
        n_mol_analyte_r = n_mol_analyte - n_mol_analyte_dr
        print("\nnº mol analyte don't reacted = " + '{:.4f} - {:.4f} = '.format(n_mol_analyte, n_mol_analyte_dr) )
        print("The mol number of the analyte that don't reacted is " + f'{n_mol_analyte_r:.4f}')

        # por fim, calcula-se o potencial utilizando a equação de Nerst
        # como essa equação é utilizada na redução, o potencial da espécie que oxida deve ter seu sinal original
        potential = titrant_rp - 0.0592/1 * math.log10(n_mol_analyte_r/n_mol_analyte_dr)
        print('E = Eº - 0.0592/nE * log Q' + ", where Q is the ratio between the reacted and the non-reacted species.")
        print('E = {} - 0.592/1 * log {:.4f}/{:.4f} = '.format(analyte_rp, n_mol_analyte_r, n_mol_analyte_dr) + f'{potential:.2f}')
        print("\nThe solution's potential with " + f'{titrant_v_used:.2f}' + " mL is " + f'{potential:.2f}' + "V.")

    else:
        print("Please, enter valid values for molarity, volume and reduction potentials.")

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


