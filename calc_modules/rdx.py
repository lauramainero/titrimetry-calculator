# função para realizar o cálculo seguindo a técnica RDX (redox: óxirredução)
# dar preferência à técnica NTR

import math

def calculate():
    if v_tit_add == 0:
        print("Não é possível calcular o potencial com 0 mL de titulante adicionado.")

    elif v_tit_add < eq_point:
        n_mol_ana = mm_ana * (v_ana / 1000)
        print('''
        nº de mol do analito = {mm_ana:.4f} * ({v_ana} / 1000) = {n_mol_ana:.4f}
        \nO número de mols do analito é {n_mol_ana:.4f}.
        ''')

        n_mol_tit = mm_tit * (v_tit_add / 1000)
        print('''
        nº de mols do titulante = {mm_tit:.4f} + ({v_tit_add} / 1000) = {n_mol_tit:.4f}
        O número de mols do titulante adicionado é {n_mol_tit:.4f}
        ''')

        n_mol_ana_ex = n_mol_ana - n_mol_tit
        print('''
        nº de mol de analito excedente = {n_mol_ana:.4f} - {n_mol_tit} = {n_mol_ana_ex:.4f}
        O número de mols do analito excedente após reação com o titulante é {n_mol_ana_ex:.4f}.
        ''')

        n_mol_ana_r = n_mol_ana - n_mol_ana_ex
        print('''
        nº de mols do analito que reagiu com o titulante = {n_mol_ana:.4f} - {n_mol_ana_ex:.4f} = {n_mol_ana_r:.4f}
        O número de mols do tampão formado é {n_mol_ana_r:.4f}.
        ''')

        pot = pr_ana - 0.0592/1 * math.log10(n_mol_ana_ex/n_mol_ana_r)
        print('''
        E = Eº - 0.0592/nE * log Q' + ", onde Q é o raio entre a parcela do analito que ficou em excesso (não reagiu) e a parcela que reagiu com o titulante.
        E = {pr_ana} - 0.592/1 * log {n_mol_ana_ex:.4f}/{n_mol_ana_r:.4f} = {pot:.2f}
        O potencial da solução com {v_tit_add:.2f} mL de titulante adicionado é {pot:.2f} V.
        '''.format(pr_ana, n_mol_ana_ex, n_mol_ana_r, pot, v_tit_add, pot))
    
    elif v_tit_add == eq_point:
        pot = (pr_ana + pr_tit)/2
        print('''
        \nE = (n * Q1 + n * Q2)/n + n
        E = (1 * {pr_ana} + 1 * {pr_tit})/1 + 1 = {pot:.2f}
        O potencial da solução com {v_tit_add:.2f} mL de titulante adicionado é {pot:.2f} V.
        ''')

    elif v_tit_add > eq_point:
        n_mol_ana = mm_ana * (v_ana / 1000)
        print('''
        nº de mols do analito = {mm_ana:.4f} * ({v_ana} / 1000) = {n_mol_ana:.4f}
        O número de mols do analito é {n_mol_ana:.4f}.
        ''')
        n_mol_tit = mm_tit * (v_tit_add / 1000)
        print('''
        nº de mols do titulante = {mm_tit:.4f} * ({v_tit_add} / 1000) = {n_mol_tit:.4f}
        O número de mols do titulante adicionado é {n_mol_tit:.4f}.
        ''')
        n_mol_tit_ex = n_mol_tit - n_mol_ana
        print('''
        nº de mols do titulante excedente = {n_mol_tit:.4f} - {n_mol_ana:.4f} = {n_mol_ana_ex:.5f}
        O número de mols do titulante excedente é {n_mol_ana_ex:.5f}.
        ''')
        n_mol_tit_r = n_mol_tit - n_mol_tit_ex
        print('''
        \nnº de mols do titulante reagiu com o analito = {n_mol_tit:.4f} - {n_mol_tit_ex:.4f} = {n_mol_tit_r:.4f}
        O número de mols da solução tampão é {n_mol_tit_r:.4f}.
        ''')
        pot = pr_tit - 0.0592/1 * math.log10(n_mol_ana_r/n_mol_ana_ex)
        print('''
        E = Eº - 0.0592/nE * log Q' + ", onde Q é o raio entre a parcela do analito que ficou em excesso (não reagiu) e a parcela que reagiu com o titulante.
        E = {} - 0.592/1 * log {pr_tit:.4f}/{n_mol_tit_ex:.4f} = {n_mol_tit_r:.2f}
        O potencial da solução com {v_tit_add:.2f} mL de titulante adicionado é {pot:.2f} V.
        ''')
        
    else:
        print("Ocorreu um erro. Please, enter valid values for molarity, volume and reduction pots.")