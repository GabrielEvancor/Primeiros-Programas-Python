###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 3 - Cartões de Crédito
# Nome: Gabriel Evangelista Correia 
# RA: 250320
###################################################


Score = int(input())
Idade = int(input())
Saldo = float(input())
Salário = float(input())

if Score<300:
	print("Cartao nao concedido")
if 300<=Score<=600:
	if Idade<30:
		print("Cartao nao concedido")
	else:
		if Salário<3000:
			print("Cartao nao concedido")
		else:
			if Saldo<7000:
				print("Cartao nao concedido")
			else:
				print("Cartao concedido")			
if Score>=600:
	if Idade<50 and Salário<2000:
		if Saldo<5000:
			print("Cartao nao concedido")
		else:
			print("Cartao concedido")	
	else:
		print("Cartao concedido")	







