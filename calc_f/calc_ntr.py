# função para realizar o cálculo seguindo a técnica de NTR (neutralização: ácido-base fortes)
# essa função em específico, por ser a mais simples, é a que tomo como base para os testes;
# se comparar às outras, essa tem muitas modificações

v_tit_add_lis, ph_lis = [], [] # lista de dados que vou usar pra construção dos gráficos; não sei se deveriam ser declaradas aqui mesmo

# PARÂMETROS: a = v_tit_add, b = eq_point, c = mm_ana, d = v_ana, e = mm_tit

def calc_ntr(a, b, c, d, e): # utilizei parâmetros na função depois de muito quebrar a cabeça com importação de módulos, não sei seria a melhor opção
	tec = 'NTR'
	if a == 0:
		ph = math.log10(c) * -1
		print(f'''
		\npH = -log{c} = {ph:.2f}
		\nO pH da solução com 0 mL de titulante adicionado é {ph:.2f}.
		''')
		ph_lis.append(ph) # adiciona o ph calculado à lista de ph
		again(tec) # chama (ou deveria chamar) a função para realizar outro cálculo
	elif a < b:
		n_mol_ana = c * (d / 1000)
		print(f'''
		\nnº de mols do analito = {c} * ({d} / 1000) = {n_mol_ana:.4f}
		\nO número de mols do analito é {n_mol_ana:.4f}
		''')
		n_mol_tit = e * (a / 1000)
		print(f'''
		\nnº de mols do titulante adicionado = {e:.4f} * ({a} / 1000) = {n_mol_tit:.4f}
		\nO número de mols do titulante adicionado é {n_mol_tit:.4f}.
		''')
		n_mol_ana_ex = n_mol_ana - n_mol_tit
		print(f'''
		\nnº mol do analito excedente (não reagiu) = {n_mol_ana:.4f} - {n_mol_tit} = {n_mol_ana_ex:.4f}
		\nO número de mols do analito excedente após a reação com o titulante é {n_mol_ana_ex:.4f}.
		''')
		n_mm_ana = n_mol_ana_ex / (d / 1000 + a / 1000)
		print(f'''
		\nNova MM do analito = {n_mol_ana_ex:.4f} / ({d} + {a}) = {n_mm_ana:.4f}
		\nA nova massa molar do analito é de {n_mm_ana:.4f} mol/L.
		''')
		ph = math.log10(n_mm_ana) * -1
		print(f'''
		\npH = -log{n_mm_ana} = {ph:.4f}
		\nO pH da solução com {a:.4f} mL de titulante adicionado é {ph:.4f}.
		''')
		ph_lis.append(ph)
		tab1(n_mol_ana, n_mol_tit, n_mol_ana_ex) # cria uma tabela no terminal para ilustrar o passo-a-passo do cálculo
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
