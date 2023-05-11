import math 

# saudações ao usuário

print("\nHello, welcome to the strong acid-base titrimetry calculator!\n")

# o usuário deverá disponibilizar o MM do titulante, MM do analito e V do analito

analyte_mm = float(input('Please, enter the analyte molarity (mol/L): '))
analyte_v = float(input('Please, enter the analyte volume (mL): '))
titrant_mm = float(input('Please, enter the titrant molarity (mol/L): '))

# o usuário receberá, então, o cálculo do ponto de equivalência

eq_point = (analyte_mm * analyte_v) / titrant_mm

# passo a passo do cálculo realizado
print("\nC1V1 = C2V2")
print("V2 = (C1V1)/C2")
print("\nV2 = " + '({} . {}) / {}'.format(analyte_mm, analyte_v, titrant_mm))
print("V2 = " + str(eq_point))
print("\nThe required volume of titrant to reach the equivalence point is " + str(eq_point) + "mL\n")

# ANOTAÇÃO: tentar formatar o número como inteiro quando ele não possuir nenhuma casa decimal significativa

# o usuário deverá disponibilizar, então, o mL de titulante que foi adicionado

titrant_v_used = float(input('Please, enter the used volume of titrant (mL): '))

# serão feitos os cálculos a partir do volume de titulante inserido em relação ao volume do ponto de equivalência

if titrant_v_used == 0:
   ph = math.log10(analyte_mm) * -1
   # passo a passo do cálculo de pH
   print("\npH = " + '-log {} = '.format(analyte_mm) + str(ph))
   print("\nThe solution's pH with 0 mL of titrant added is " + str(ph))

# o pH é calculado em função da concentração de H3O+ proveniente do ácido que não reagiu com a base
elif titrant_v_used < eq_point:
    
    # primeiramente, é calculado o nº de mols do analito (H3O+)
    n_mol_analyte = analyte_mm * (analyte_v / 1000)
    print("\nnº mol H3O+ = " + '{} * ({} / 1000) = '.format(f'{analyte_mm:.4f}', analyte_v) + f'{n_mol_analyte:.4f}')
    print("The mol number of the analyte is " + f'{n_mol_analyte:.4f}')

    # em seguida, calcula-se o nº de mols do titulante adicionado (OH-)
    n_mol_titrant = titrant_mm * (titrant_v_used / 1000)
    print("\nnº mol OH- = " + '{} * ({} / 1000) = '.format(titrant_mm, titrant_v_used) + str(n_mol_titrant))
    print("The mol number of the titrant volume used is " + str(n_mol_titrant))

    # agora, calcula-se o número de mols de H3O+ livre restante no analito
    n_mol_analyte_dr = n_mol_analyte - n_mol_titrant
    print("\nnº mol H3O+ left = " + '{} - {} = '.format(f'{n_mol_analyte:.4f}', n_mol_titrant) + f'{n_mol_analyte_dr:.4f}')
    print("The mol number of the analyte amount that don't reacted with the titrant is " + f'{n_mol_analyte_dr:.4f}')
    
    # com o número de mols, encontra-se a nova concentração utilizando tambem o novo volume total
    analyte_nmm = n_mol_analyte_dr / (analyte_v / 1000 + titrant_v_used / 1000)
    print("\nNew H3O+ molarity = " + '{} / ({} + {}) = '.format(f'{n_mol_analyte_dr:.4f}', analyte_v, titrant_v_used) + f'{analyte_nmm:.4f}')
    print("The new molarity of the analyte is " + f'{analyte_nmm:.4f}' + " mol/L.")
    
    # com a concentração, é possível achar o pH com adição de 10 mL de ácido
    ph = math.log10(analyte_nmm) * -1
    print("\npH = " + '-log {} = '.format(f'{analyte_nmm:.4f}') + f'{ph:.4f}')
    print("\nThe solution's pH with " + str(titrant_v_used) + " mL of titrant added is " + f'{ph:.4f}')

# o pH é calculado em função do equilíbrio de H2O
elif titrant_v_used == eq_point:
    
    # primeiramente, é calculado o nº de mols do analito (H3O+)
    n_mol_analyte = analyte_mm * (analyte_v / 1000)
    print("\nnº mol H3O+ = " + '{} * ({} / 1000) = '.format(analyte_mm, analyte_v) + str(n_mol_analyte))
    print("The mol number of the analyte is " + str(n_mol_analyte))
    
    # como o mL adicionado e as molaridades são as mesmas, temos que nº mol H3O+ = º mol OH-
    print("\n2 H2O \u21CB H3O+ + OH-")
    print("H3O+ = OH- = 1 \u00D7 10e-7")

    # portanto, a nova molaridade será dada através do equilíbrio iônico (Kw) da água, que é tabelado
    kw = 1*10**-14
    ph = math.log10(kw) * -1
    print("\npH = " + '-log {} = '.format('1 \u00D7 10e-7') + str(ph))
    print("\nThe solution's pH on the equivalence point is " + str(ph) + ".")

# como já não há mais ácido para reagir, o pH é calculado em função do pOH, a concentração de OH- proveniente do excesso adicionado
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
    print("ainda vou escrever aqui")