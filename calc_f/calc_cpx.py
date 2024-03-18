# função para realizar o cálculo seguindo a técnica de CPX (complexação)
# dar preferência à técnica NTR

import math

def calc_cpx():
    # serão feitos os cálculos a partir do volume de titulante inserido em relação ao volume do ponto de equivalência
    # como não há EDTA, a concentração de analito livre é a concentração dada
    if v_tit_add == 0:
        p_ana = math.log10(mm_ana) * -1
        print("Analyte molarity = " + '{}'.format(mm_ana))
        print("")
        print("The free molarity of the analyte is " + f'{p_ana}' + ".")
        
    elif v_tit_add < eq_point:
        # primeiramente, é calculado o nº de mols do analito 
        n_mol_ana = mm_ana * (v_ana / 1000)
        print("\nnº mol H3O+ = " + '{:.4f} * ({} / 1000) = '.format(mm_ana, v_ana) + f'{n_mol_ana:.4f}')
        print("The mol number of the analyte is " + f'{n_mol_ana:.4f}' + ".")

        # em seguida, calcula-se o nº de mols de EDTA adicionado
        n_mol_tit = mm_tit * (v_tit_add / 1000)
        print("\nnº mol titrant = " + '{} * ({} / 1000) = '.format(mm_tit, v_tit_add) + f'{n_mol_tit:.4f}')
        print("The mol number of the titrant volume used is " + f'{n_mol_tit:.4f}' + ".")

        # agora, calcula-se o número de mols do analito livre restante na solução
        n_mol_ana_ex = n_mol_ana - n_mol_tit
        print("\nnº mol analyte left = " + '{:.4f} - {} = '.format(n_mol_ana, n_mol_tit) + f'{n_mol_ana_ex:.4f}')
        print("The mol number of the analyte amount that don't reacted with the titrant is " + f'{n_mol_ana_ex:.4f}' + ".")
    
        # com o número de mols, encontra-se a nova concentração utilizando tambem o novo volume total
        n_mm_ana = n_mol_ana_ex / (v_ana / 1000 + v_tit_add / 1000)
        print("\nNew analyte molarity = " + '{:.4f} / ({} + {}) = '.format(n_mol_ana_ex, v_ana, v_tit_add) + f'{n_mm_ana:.2e}')
        print("The new molarity of the analyte is " + f'{n_mm_ana:.2e}' + " mol/L.")
    
        # com a concentração, é possível achar o pAnalito
        p_ana = math.log10(n_mm_ana) * -1
        print("\nPotential = " + '-log {:.2e} = '.format(n_mm_ana) + f'{p_ana:.2f}')
        print("\nThe solution's analyte potential with " + f'{v_tit_add:.2f}' + " mL of titrant added is " + f'{p_ana:.2f}' + ".")

    elif v_tit_add == eq_point:
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

    # elif v_tit_add > eq_point:

    # else: