import sqlite3
from datetime import datetime

#lista de serviços com preços
lista_servicos = [["xerox p&b",0.25],["xerox col",0.50],["foto3x4",8.00],["2° via de contas",2.00],["folhaA4",0.10],["envelopeA4",0.70],["curriculo",2.00],["impressao p&b",0.50],["impressao col",1.00],["musica no pendrive",0.75],["digitaçao",3.50],["preco alternativo", 0,]]

#serviços escolhidos
servicos_escolhidos = []
lista_vezes = []

#listas para facilitar ainda mais o trabalho
l_servico = []
l_val_uni = []
l_quant_vezes = []
l_multi = []
l_data = []

#variaveis globais
n_vezes = 0
valor_unitario = 0
valor_multi = 0
total = 0
vezes = 0
servico = 0




def grava():
	#banco de dados
	global n_vezes
	conn = sqlite3.connect("dados_loja.db")
	cursor = conn.cursor()
	n = 1
	m = 0
	print(l_servico[m])
	while n <= len(l_servico):
		cursor.execute('INSERT INTO registro (servico, valor_unitario, quant_vezes, valor_final, data) VALUES (?,?,?,?,?)',
		(l_servico[n-1], l_val_uni[n-1], l_quant_vezes[n-1], l_multi[n-1], l_data[n-1]))
		n += 1
		m += 1
		conn.commit()
		
	conn.close()

def menu(lista):
	"""menu do programa"""
	numero = 0
	print(" {}{}{}\n {}".format("Serviços", " "*18,"Preço","-"*31))
	for item in lista:
		servico = item[0]
		preco = item[1] 
		print("{:2} {:25}{:3.2f}".format(numero,servico,preco))
		numero += 1
	numero = 0

def data():
	agora = datetime.now()
	data_hora = agora.strftime("%m/%d/%Y %H:%M")
	l_data.append(data_hora)

def seleciona_servico():
	global servico
	global n_vezes
	"""seleciona o servico desejado"""
	opcao = int(input("\nEscolha o serviço: "))
	data()
	l_servico.append(lista_servicos[opcao][0])
	l_val_uni.append(lista_servicos[opcao][1])
	servico = lista_servicos[opcao]
	vezess()
	lista_vezes.append(vezes)
	servicos_escolhidos.append(servico)
	calcula()
	
	r = input("Deseja adicionar outro servico: s/n ")
	if r in "Ss":
		n_vezes += 1
		seleciona_servico()
	else:
		exibe()
		troco()
		grava()

def vezess():
	"""pergunta ao usuario quantas vezes ele deseja o servico"""
	global vezes
	vezes = int(input("Informe a quantidade: "))
	l_quant_vezes.append(vezes)
	print()

def exibe():
	"""exibe o valor total, valor multiplicado e a lista de servicos escolhidos"""
	global vezes
	global valor_multi
	print(" Servicos selecionados\n--------------------")
	print(" {:20}{:20}{:20}{:20}".format("Servico","valor unitario", "vezes", "valor multiplicado"))
	for i,j in zip(servicos_escolhidos,lista_vezes):
		print(" {:20}{}{:>20}{:>23}".format(i[0],i[1],j,i[1]*j))
	print()
	print("Total: ",total)
	
def calcula():
	"""calcula o valor do servico"""
	global valor_unitario
	global valor_multi
	global total
	global vezes
	global servico
	valor_unitario = servico[1]
	if vezes > 1: 
		valor_multi = valor_unitario * lista_vezes[n_vezes]
		l_multi.append(valor_multi)
		total += valor_multi
	else:
		total += valor_unitario
	
def troco():
	global total
	recebido = float(input("Digite o valor recebido: "))
	troco = recebido - total
	print()
	print("Troco: ",troco)
	
	
menu(lista_servicos)
seleciona_servico()
	

