###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 6 - O Porteiro do Castelo
# Nome:Gabriel Evangelista Correia 
# RA:250320
###################################################


senha = [int(i) for i in input().split()]
lista = sorted(senha)
achou = False
n = len(senha) 
for i in range(len(senha)):
	senha.insert(n+1,senha[0])
	senha.remove(senha[0])
	if senha == lista:
		achou = True
		print("Klift, Kloft, Still, a porta se abriu")
		break	
if achou == False: 
	print("Senha incorreta")

				 		
	










