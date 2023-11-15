###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 11 - Fuga de Nova coord2ork
# Nome:Gabriel Evangelista Correia 
# RA:250320 
###################################################

lista1 = []
lista2 = []
ajuda = input().split()
N_colunas = len(ajuda)
soma_linha = 0
cidade = []

while ajuda[0].isnumeric() == False:
    cidade.append(ajuda)
    soma_linha = soma_linha + 1
    ajuda = input().split()
n = int(ajuda[0])

def busca(coord1,coord2,temporizador):
    temporizador = temporizador + 1 
    fugiu = False
    if cidade[coord1][coord2] == "O":
        coord2 = coord2 - 1
    elif cidade[coord1][coord2] == "L":
        coord2 = coord2 + 1
    elif cidade[coord1][coord2] == "S":
        coord1 = coord1 + 1        
    elif cidade[coord1][coord2] == "N":
        coord1 = coord1 - 1    
    if coord2 == -1:
       print("Fuga pelo oeste.")
       fugiu = True

    if coord2 == N_colunas:
       print("Fuga pelo leste.")
       fugiu = True

    if coord1 == soma_linha:
       print("Fuga pelo sul.")
       fugiu = True       

    if coord1 == -1:
        print("Fuga pelo norte.")
        fugiu = True
    
    if temporizador > soma_linha*N_colunas:
        print("Resgate aereo solicitado.")
        fugiu = True
    if not fugiu:
        busca(coord1,coord2,temporizador)

for i in range(n):
    L, C = input().split()
    lista1.append(int(L))
    lista2.append(int(C))

for i in range(n):
    busca(lista1[i], lista2[i], -1)
