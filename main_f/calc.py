import math
from main_f.tab_f import tab1, tab2, tab3
from main_f.titrant_f import titrant
from main_f.again_f import again
from time import sleep
global v_tit_add

v_tit_add_lis, ph_lis = [], []

# a = v_tit_add, b = eq_point, c = mm_ana, d = v_ana, e = mm_tit

def calc_ntr(a, b, c, d, e):
	tec = 'NTR'
	if a == 0:
		ph = math.log10(c) * -1
		print(f'''
		\npH = -log{c} = {ph:.2f}
		\nO pH da solução com 0 mL de titulante adicionado é {ph:.2f}.
		''')
		ph_lis.append(ph)
		again(tec)
	elif a < b:
		n_mol_ana = c * (d / 1000)
		print(f'''
		nº de mols do analito = {c} * ({d} / 1000) = {n_mol_ana:.4f}
		O número de mols do analito é {n_mol_ana:.4f}
		''')
		sleep(3)
		n_mol_tit = e * (a / 1000)
		print(f'''
		nº de mols do titulante adicionado = {e:.4f} * ({a} / 1000) = {n_mol_tit:.4f}
		O número de mols do titulante adicionado é {n_mol_tit:.4f}.
		''')
		sleep(3)
		n_mol_ana_ex = n_mol_ana - n_mol_tit
		print(f'''
		nº mol do analito excedente (não reagiu) = {n_mol_ana:.4f} - {n_mol_tit} = {n_mol_ana_ex:.4f}
		O número de mols do analito excedente após a reação com o titulante é {n_mol_ana_ex:.4f}.
		''')
		sleep(3)
		tab1(n_mol_ana, n_mol_tit, n_mol_ana_ex) # tabela apresentando de maneira dinamica os valores ja calculados
		sleep(3)
		n_mm_ana = n_mol_ana_ex / (d / 1000 + a / 1000)
		print(f'''
		Nova MM do analito = {n_mol_ana_ex:.4f} / ({d} + {a}) = {n_mm_ana:.4f}
		A nova massa molar do analito é de {n_mm_ana:.4f} mol/L.
		''')
		sleep(3)
		ph = math.log10(n_mm_ana) * -1
		print(f'''
		pH = -log{n_mm_ana:.4f} = {ph:.4f}
		O pH da solução com {a:.4f} mL de titulante adicionado é {ph:.4f}.
		''')
		sleep(3)
		ph_lis.append(ph)
		again(tec)
	elif a == b:
		n_mol_ana = c * (d / 1000)
		print(f'''
		\nnº mol do analito = {c:.4f} * ({d} / 1000) = {n_mol_ana:.4f}
		\nO número de mols do analito é {n_mol_ana:.4f}
		''')
		print('''
		2 H2O \u21CB H3O+ + OH-
		H3O+ = OH- = 1 * 10e-7
		''')
		ph = math.log10(10**-7) * -1
		print(f'''
		\npH = -log 10e-7 = {ph:.3f}
		\nO pH da solução em seu ponto de equivalência é {ph:.3f}.
		''')
		ph_lis.append(ph)
		tab2(n_mol_ana)
		again(tec)
	elif a > b:
		n_mol_ana = c * (d / 1000)
		print(f'''
		\nnº mol do analito = {c:.4f} * ({d} / 1000) = {n_mol_ana:.4f}
		\nO número de mols do analito é {n_mol_ana:.4f}
		''')
		n_mol_tit = e * (a / 1000)
		print(f'''
		\nnº mol do titulante = {e:.4f} * ({a} / 1000) = {n_mol_tit:.4f}
		\nO número de mols do titulante adicionado é {n_mol_tit:.4f}.
		''')
		n_mol_tit_ex = n_mol_tit - n_mol_ana
		print(f'''
		\nnº mol do titulante excedente = {n_mol_tit:.4f} - {n_mol_ana} = {n_mol_tit_ex:.4f}
		\nO número de mols do titulante excedente após a reação com o analito é {n_mol_tit_ex:.4f}.
		''')
		n_mm_tit = n_mol_tit_ex / (d / 1000 + a / 1000)
		print(f'''
		\nNova MM do excesso de titulante = {n_mol_tit_ex:.4f} / ({d} + {a}) = {n_mm_tit:.4f}
		\nA massa molar do excesso de titulante é de {n_mm_tit:.4f} mol/L.
		''')
		ph = math.log10(n_mm_tit) * -1
		print(f'''
		\npH = -log{n_mm_tit} = {ph:.4f}
		\nO pH da solução com {a:.4f} mL de titulante adicionado é {ph:.4f}.
		''')
		ph_lis.append(ph)
		tab3(n_mol_ana, a, n_mol_tit_ex)
		again(tec)
