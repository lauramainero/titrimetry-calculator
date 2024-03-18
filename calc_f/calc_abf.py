# função para realizar o cálculo seguindo a técnica de ABF (ácido fraco/base forte)
# dar preferência à técnica NTR

import math

def calc_abf():
    if v_tit_add == 0:
        pka = math.log10(ka) * -1
        print('''
        pKa = -log {ka:.0e} = {pka:.4f}
        O valor do pKa é {pka:.4f}.
        ''')

        mm_ka = ka * mm_ana
        n_mm_ana = math.sqrt(mm_ka)
        ph = math.log10(n_mm_ana) * -1
        print('''
        HA + H2O \u21CB  H3O+ + A- 
        Ka = ([H3O+] * [A-]) / [HA]
        [H3O+] = [A-] = [H3O+]\u00b2
        ''') # onde HA = ácido fraco e A- dissociação do ácido fraco

        print('''
        {ka:.0e} = ([H3O+] * [A-]) / {mm_ana}
        [H3O+]\u00b2 = {ka:.0e} * {mm_ana} = {mm_ka:.4e}
        [H3O+] = \u221A{mm_ka:.4e} = {ph:.2f}
        \nO pH da solução com 0 mL de titulante adicionado é {ph:.2f}. 
        ''')

    elif v_tit_add < eq_point:
        print("\nHA + OH- \u21CB  A- + H2O") 

        n_mol_ana = mm_ana * (v_ana / 1000)
        print('''
        nº de íons H3O+ = {mm_ana} / ({v_ana:.4f} / 1000) = {n_mol_ana:.4f}
        O número de mols do analito é {n_mol_ana:.4f}.
        ''')

        n_mol_tam = mm_tit * (v_tit_add / 1000)
        print('''
        nº de mols do tampão = {mm_tit} * ({v_tit_add} / 1000) = {n_mol_tam:.4f}
        O número de mols do tampão formado é {n_mol_tam:.4f}.
        ''')

        n_mol_ana_ex = n_mol_ana - n_mol_tam
        print('''
        nº de mols dos íons H3O+ excedentes = {n_mol_ana:.4f} - {n_mol_tam:.4f} = {n_mol_ana_ex:.4f}
        O número de mols do analito excedente (não reagiu com o titulante) é {n_mol_ana_ex:.4f}.
        ''')

        n_mm_tam = n_mol_tam / (v_ana / 1000 + v_tit_add / 1000)
        n_mm_ana = n_mol_ana_ex / (v_ana / 1000 + v_tit_add / 1000)
        print('''
        Massa molar do tampão = {:.4f} / ({} + {}) = {:.4e}
        Nova ma
        ''') # tava passando tudo pra triple quote mas cansei e terminei aqui

        print("\nTampon molarity = " + '{:.4f} / ({} + {}) = '.format(n_mol_tam, v_ana, v_tit_add) + f'{n_mm_tam:.4e}')
        print("\nNew H3O+ molarity = " + '{:.4f} / ({} + {}) = '.format(n_mol_ana_ex, v_ana, v_tit_add) + f'{n_mm_ana:.4e}')
        print("\nThe molarity of the tampon is " + f'{n_mm_tam:.4e}' + " mol/L.")
        print("\nThe new molarity of the analyte is " + f'{n_mm_ana:.4e}' + " mol/L.")

        pka = math.log10(ka) * -1
        print('\npKa = -log {:.0e} = '.format(ka) + f'{pka:.4f}')
        print("\nThe pKa value is " + f'{pka:.4f}')

        ph = pka + math.log10(n_mm_tam / n_mm_ana)
        print("\npH = " + 'pKa + log {:.3e} / {:.3e} = '.format(n_mm_tam, n_mm_ana) + f'{ph:.4f}')
        print("\nThe solution's pH with " + f'{v_tit_add:.2f}' + " mL of titrant added is " + f'{ph:.4f}' + ".")
    
    elif v_tit_add == eq_point:
        # passo a passo do cálculo para achar o pKa
        pka = math.log10(ka) * -1
        print('\npKa = -log {:.0e} = '.format(ka) + f'{pka:.4f}')
        print("\nThe pKa value is " + f'{pka:.4f}')
    
        kw = 1*10**-14
        kb = kw / ka
        print("\nKa * Kb = Kw")
        print("Kb = Kw / Ka")

        print('Kb = {:.3e} / {:.3e} = '.format(kw, ka) + f'{kb:.3e}')
        print("\nThe Kb value is " + f'{kb:.3e}')
    
        n_mol_tam = mm_tit * (v_tit_add / 1000)
        print("\nnº mol H3O+ = " + '{:.4f} * ({} / 1000) = '.format(mm_tit, v_tit_add) + f'{n_mol_tam:.4f}')
        print("The mol number of the analyte is " + f'{n_mol_tam:.4f}' + ".")

        n_mm_tam = n_mol_tam / (v_ana / 1000 + v_tit_add / 1000)
        print("\n Tampon molarity = " + '{:.4f} / ({} + {}) = '.format(n_mol_tam, v_ana, v_tit_add) + f'{n_mm_tam:.4e}')
    
        print("\nKb = ([HA] * [OH-]) / [A-]")
        print("On the equivalence point, [HA] = [OH-]")
        print("Kb = [OH-]\u00b2 / [A-]")
        print("[OH-]\u00b2 = [A-] * Kb")

        kb_mm = n_mm_tam * kb
        n_mm_ana = n_mm_tam
        n_mm_ana = math.sqrt(kb_mm) # como [HA] = [A-], pode ser feita a equivalência com a molaridade do analito
        poh = math.log10(n_mm_ana) * -1

        print('\n[OH-]\u00b2 = {:.3e} * {:.3e} = '.format(n_mm_tam, kb) + f'{kb_mm:.4e}')
        print('[OH-] = \u221A{:.4e} = '.format(kb_mm) + f'{n_mm_ana:.4f}')

        print("pOH = -log [OH-]")
        print('pOH = -log {:.4e} = '.format(n_mm_ana) + f'{poh:.4f}')
    
        print("\nThe solution's pOH with " + f'{v_tit_add:.2f}' + " of titrant added is " + f'{poh:.4f}' + ".")
    
        print("\npH + pOH = 14")
        print("pH = 14 - pOH")

        ph = 14 - poh
        print("\npH = 14 - " + f'{poh:.4f}' + " = " + f'{ph:.4f}')
        print("\nThe solution's pH with " + f'{v_tit_add:.2f}' + " mL of titrant added is " + f'{ph:.4f}' + ".")

    elif v_tit_add > eq_point:
        n_mol_ana = mm_ana * (v_ana / 1000)
        print("\nnº mol H3O+ = " + '{:.4f} * ({:.4f} / 1000) = '.format(mm_ana, v_ana) + f'{n_mol_ana:.4f}')
        print("The mol number of the analyte is " + f'{n_mol_ana:.4f}' + ".")

        n_mol_tit = mm_tit * (v_tit_add / 1000)
        print("\nnº mol OH- = " + '{:.4f} * ({:.4f} / 1000) = '.format(mm_tit, v_tit_add) + f'{n_mol_tit:.4f}')
        print("The mol number of the titrant volume used is " + f'{n_mol_tit:.4f}' + ".")

        n_mol_analyte_ex = n_mol_tit - n_mol_ana
        print("\nnº mol H3O+ left = " + '{:.4f} - {:.4f} = '.format(n_mol_tit, n_mol_ana) + f'{n_mol_analyte_ex:.4f}')
        print("The mol number of the titrant excess amount is " + f'{n_mol_analyte_ex:.4f}' + ".")
    
        titrant_nmm = n_mol_analyte_ex / (v_ana / 1000 + v_tit_add / 1000)
        print("\nMM titrant excess = " + '{:.4f} / ({:.4f} + {:.4f}) = '.format(n_mol_analyte_ex, v_ana, v_tit_add) + f'{titrant_nmm:.4f}')
        print("The molarity of the titrant excess amount is " + f'{titrant_nmm:.4f}' + " mol/L.")
    
        poh = math.log10(titrant_nmm) * -1
        print("\npOH = " + '-log {} = '.format(f'{titrant_nmm:.4f}') + f'{poh:.4f}')
        print("\nThe solution's pOH with " + f'{v_tit_add:.2f}' + " mL of titrant added is " + f'{poh:.4f}' + ".")

        print("\npH + pOH = 14")
        print("pH = 14 - pOH")

        ph = 14 - poh
        print("\npH = 14 - " + f'{poh:.4f}' + " = " + f'{ph:.4f}')
        print("\nThe solution's pH with " + f'{v_tit_add:.2f}' + " mL of titrant added is " + f'{ph:.4f}' + ".")

    else:
        print("Please, enter valid values for molarity and volume.")