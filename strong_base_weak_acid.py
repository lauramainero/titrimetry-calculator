import math

def welcome():
    # saudações ao usuário
    print("\nHello, welcome to the strong acid-base titrimetry calculator!")

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

information()

def titrant():
    #o usuário deverá disponibilizar, então, o mL de titulante que foi adicionado
    global titrant_v_used
    titrant_v_used = float(input('\nPlease, enter the used volume of titrant (mL): '))

titrant()

def calculate():
    # serão feitos os cálculos a partir do volume de titulante inserido em relação ao volume do ponto de equivalência
    # o pH será dado pela dissociação do ácido fraco
    if titrant_v_used == 0:

        ka = float(eval(input('\nPlease, enter the Ka value: ')))
        # passo a passo do cálculo para achar o pKa
        pka = math.log10(ka) * -1
        print('\npKa = -log {:.0e} = '.format(ka) + f'{pka:.4f}')
        print("\nThe pKa value is " + f'{pka:.4f}')

        # variáveis para os cálculos
        ka_mm = ka * analyte_mm
        analyte_nmm = math.sqrt(ka_mm)
        ph = math.log10(analyte_nmm) * -1

        # explicações sobre as equivalências e relações
        print("\nHA + H2O \u21CB  H3O+ + A-") # onde HA = ácido fraco e A- dissociação do ácido fraco
        print("\nKa = ([H3O+] * [A-]) / [HA]")
        print("\n[H3O+] = [A-] = [H3O+]\u00b2")

        # amostragem de resultados
        print('\n{:.0e} = '.format(ka) + "([H3O+] * [A-])" ' / {}'.format(analyte_mm))
        print('[H3O+]\u00b2 = {:.0e} * {} = '.format(ka, analyte_mm) + f'{ka_mm:.4e}')
        print('[H3O+] = \u221A{:.4e} = '.format(ka_mm) + f'{ph:.4f}')

        print("\nThe solution's pH with 0 mL of titrant added is " + f'{ph:.4f}')
    
    # o pH será calculado com base na solução tampão formada
    elif titrant_v_used < eq_point:
        print("\nHA + OH- \u21CB  A- + H2O") 

        # primeiramente, é calculado o nº de mols do analito (HA)
        n_mol_analyte = analyte_mm * (analyte_v / 1000)
        print("\nnº mol H3O+ = " + '{} * ({} / 1000) = '.format(f'{analyte_mm:.4f}', analyte_v) + f'{n_mol_analyte:.4f}')
        print("The mol number of the analyte is " + f'{n_mol_analyte:.4f}')
   
        # em seguida, é calculado o nº de mols do tampão formado (A-) com o agente limitante sendo a base
        n_mol_tampon = titrant_mm * (titrant_v_used / 1000)
        print("\nnº mol tampon = " + '{} * ({} / 1000) = '.format(f'{titrant_mm:.4f}', titrant_v_used) + f'{n_mol_tampon:.4f}')
        print("The mol number of the tampon is " + f'{n_mol_tampon:.4f}')
   
        # agora, calcula-se o número de mols de H3O+ livre restante no analito
        n_mol_analyte_dr = n_mol_analyte - n_mol_tampon
        print("\nnº mol H3O+ left = " + '{} - {} = '.format(f'{n_mol_analyte:.4f}', f'{n_mol_tampon:.4f}') + f'{n_mol_analyte_dr:.4f}')
        print("The mol number of the analyte amount that don't reacted with the titrant is " + f'{n_mol_analyte_dr:.4f}')
   
        # com o número de mols, encontra-se a nova concentração tanto do tampão quanto do ácido que não reagiu
        tampon_nmm = n_mol_tampon / (analyte_v / 1000 + titrant_v_used / 1000)
        analyte_nmm = n_mol_analyte_dr / (analyte_v / 1000 + titrant_v_used / 1000)
        print("\nTampon molarity = " + '{} / ({} + {}) = '.format(f'{n_mol_tampon:.4f}', analyte_v, titrant_v_used) + f'{tampon_nmm:.4e}')
        print("\nNew H3O+ molarity = " + '{} / ({} + {}) = '.format(f'{n_mol_analyte_dr:.4f}', analyte_v, titrant_v_used) + f'{analyte_nmm:.4e}')
        print("\nThe molarity of the tampon is " + f'{tampon_nmm:.4e}' + " mol/L.")
        print("\nThe new molarity of the analyte is " + f'{analyte_nmm:.4e}' + " mol/L.")

        ka = float(eval(input('\nPlease, enter the Ka value: ')))
        # passo a passo do cálculo para achar o pKa
        pka = math.log10(ka) * -1
        print('\npKa = -log {:.0e} = '.format(ka) + f'{pka:.4f}')
        print("\nThe pKa value is " + f'{pka:.4f}')

        # com a concentração de ambos, é possível achar o pH antes do ponto de equivalência
        ph = pka + math.log10(tampon_nmm / analyte_nmm)
        print("\npH = " + 'pKa + log {:.3e} / {:.3e} = '.format(tampon_nmm, analyte_nmm) + f'{ph:.4f}')
        print("\nThe solution's pH with " + str(titrant_v_used) + " mL of titrant added is " + f'{ph:.4f}')
    
    # o cálculo do pH será feito com base na hidrólise do sal formado
    elif titrant_v_used == eq_point:
    
        ka = float(eval(input('\nPlease, enter the Ka value: ')))
        # passo a passo do cálculo para achar o pKa
        pka = math.log10(ka) * -1
        print('\npKa = -log {:.0e} = '.format(ka) + f'{pka:.4f}')
        print("\nThe pKa value is " + f'{pka:.4f}')
    
        # cálculo do Kb
        # constante de ionização da água Kw = 1 * 10e-14
        kw = 1*10**-14
        kb = kw / ka
        print("\nKa * Kb = Kw")
        print("Kb = Kw / Ka")

        print('Kb = {:.3e} / {:.3e} = '.format(kw, ka) + f'{kb:.3e}')
        print("\nThe Kb value is " + f'{kb:.3e}')
    
        # é calculado o nº de mols do tampão formado (A-) com o agente limitante sendo a base
        n_mol_tampon = titrant_mm * (titrant_v_used / 1000)
        print("\nnº mol H3O+ = " + '{} * ({} / 1000) = '.format(f'{titrant_mm:.4f}', titrant_v_used) + f'{n_mol_tampon:.4f}')
        print("The mol number of the analyte is " + f'{n_mol_tampon:.4f}')

        # com o número de mols, encontra-se a nova concentração do tampão
        tampon_nmm = n_mol_tampon / (analyte_v / 1000 + titrant_v_used / 1000)
        print("\n Tampon molarity = " + '{} / ({} + {}) = '.format(f'{n_mol_tampon:.4f}', analyte_v, titrant_v_used) + f'{tampon_nmm:.4e}')

    
        print("\nKb = ([HA] * [OH-]) / [A-]")
        print("On the equivalence point, [HA] = [OH-]")
        print("Kb = [OH-]\u00b2 / [A-]")
        print("[OH-]\u00b2 = [A-] * Kb")

        kb_mm = tampon_nmm * kb
        analyte_nmm = tampon_nmm
        analyte_nmm = math.sqrt(kb_mm) # como [HA] = [A-], pode ser feita a equivalência com a molaridade do analito
        poh = math.log10(analyte_nmm) * -1

        print('\n[OH-]\u00b2 = {:.3e} * {:.3e} = '.format(tampon_nmm, kb) + f'{kb_mm:.4e}')
        print('[OH-] = \u221A{:.4e} = '.format(kb_mm) + f'{analyte_nmm:.4f}')

        print("pOH = -log [OH-]")
        print('pOH = -log {:.4e} = '.format(analyte_nmm) + f'{poh:.4f}')
    
        print("\nThe solution's pOH with " + str(titrant_v_used)+ " of titrant added is " + f'{poh:.4f}' + ".")
    
        # a partir das relações entre pH e pOH, é possível encontrar o valor de pH da solução com adição 102 mL de titulante
        print("\npH + pOH = 14")
        print("pH = 14 - pOH")

        ph = 14 - poh
        print("\npH = 14 - " + f'{poh:.4f}' + " = " + f'{ph:.4f}')
        print("\nThe solution's pH with " + str(titrant_v_used) + " mL of titrant added is " + f'{ph:.4f}' + ".")

    # comentario que ainda vou adicionar
    elif titrant_v_used > eq_point:

        # primeiramente, é calculado o nº de mols do analito (H3O+)
        n_mol_analyte = analyte_mm * (analyte_v / 1000)
        print("\nnº mol H3O+ = " + '{} * ({} / 1000) = '.format(f'{analyte_mm:.4f}', f'{analyte_v:.4f}') + f'{n_mol_analyte:.4f}')
        print("The mol number of the analyte is " + f'{n_mol_analyte:.4f}' + ".")

        # em seguida, calcula-se o nº de mols do titulante (OH-)
        n_mol_titrant = titrant_mm * (titrant_v_used / 1000)
        print("\nnº mol OH- = " + '{} * ({} / 1000) = '.format(f'{titrant_mm:.4f}', f'{titrant_v_used:.4f}') + f'{n_mol_titrant:.4f}')
        print("The mol number of the titrant volume used is " + f'{n_mol_titrant:.4f}' + ".")

        # agora, calcula-se o número de mols de OH- em excesso no analito
        n_mol_analyte_ex = n_mol_titrant - n_mol_analyte
        print("\nnº mol H3O+ left = " + '{} - {} = '.format(f'{n_mol_titrant:.4f}', f'{n_mol_analyte:.4f}') + f'{n_mol_analyte_ex:.4f}')
        print("The mol number of the titrant excess amount is " + f'{n_mol_analyte_ex:.4f}' + ".")
    
        # com o número de mols, encontra-se a concentração do excesso de OH- utilizando tambem o novo volume total
        titrant_nmm = n_mol_analyte_ex / (analyte_v / 1000 + titrant_v_used / 1000)
        print("\nMM titrant excess = " + '{} / ({} + {}) = '.format(f'{n_mol_analyte_ex:.4f}', f'{analyte_v:.4f}', f'{titrant_v_used:.4f}') + f'{titrant_nmm:.4f}')
        print("The molarity of the titrant excess amount is " + f'{titrant_nmm:.4f}' + " mol/L.")
    
        # com a concentração, é possível achar o pOH
        poh = math.log10(titrant_nmm) * -1
        print("\npOH = " + '-log {} = '.format(f'{titrant_nmm:.4f}') + f'{poh:.4f}')
        print("\nThe solution's pOH with " + str(titrant_v_used) + " mL of titrant added is " + f'{poh:.4f}' + ".")

        # a partir das relações entre pH e pOH, é possível encontrar o valor de pH da solução com adição 102 mL de titulante
        print("\npH + pOH = 14")
        print("pH = 14 - pOH")

        ph = 14 - poh
        print("\npH = 14 - " + f'{poh:.4f}' + " = " + f'{ph:.4f}')
        print("\nThe solution's pH with " + str(titrant_v_used) + " mL of titrant added is " + f'{ph:.4f}' + ".")

    else:
        print("Please, enter valid values for molarity and volume.")

    # função again() para o usuário calcular novamente
    def again():
        calc_again = input('''
        Do you want to calculate again?
        Please, type Y for yes or N for no.
        ''')

        if calc_again.upper() == 'Y':
            titrant()
            calculate()

        elif calc_again.upper() == 'N':
            print("T\nThank you for using the titrimetry calculator, see you later!")

        else:
            again()
    again()
calculate()