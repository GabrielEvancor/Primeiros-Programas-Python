#####################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 9 - Jogos Olímpicos
# Nome:Gabriel Evangelista Correia 
# RA:250320 
#####################################################
 
from collections import Counter 
lista = [int(x) for x in input().split()]
N = lista[0]

ranking = [input().split() for i in range(N)]

p_ouros = []
for i in range(N):
	p_ouros.append(ranking[i][1]) 
O = Counter(p_ouros)
for i in O.keys():
	O[i] = O[i]*lista[1]

p_prata = []
for i in range(N):
	p_prata.append(ranking[i][2])	
P = Counter(p_prata)
for i in P.keys():
	P[i] = P[i]*lista[2]
	
p_bronze = []
for i in range(N):
	p_bronze.append(ranking[i][3])
B = Counter(p_bronze)
for i in B.keys():
	B[i] = B[i]*lista[3]

main_dictionary = O + P + B

lista1 = []
maior_pontuação = main_dictionary[max(main_dictionary, key = main_dictionary.get)]
for i in main_dictionary.keys():
	if main_dictionary[i] == maior_pontuação:
		lista1.append(i)
aux = 0
lista1.sort()
while aux<len(lista1):
    print(lista1[aux], maior_pontuação)
    for i in range(N):
        if lista1[aux] == ranking[i][1]:
            print(ranking[i][0])
    aux = aux + 1



	






