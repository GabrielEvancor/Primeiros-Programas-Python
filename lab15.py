###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 15 - Fuga de Nova York II
# Nome:Gabriel Evangelista Correia 
# RA:250320
###################################################

lista1 = []
lista2 = []
ajuda = input().split()
N_colunas = len(ajuda)
soma_linha = 0 
mapa = []

while ajuda[0].isnumeric() == False:
    mapa.append(ajuda)
    soma_linha = soma_linha + 1
    ajuda = input().split()
n = int(ajuda[0])

def busca(mapa,L,C):
    if C == -1:
       return True
    
    if C == N_colunas:       
        return True

    if L == soma_linha:      
        return True       

    if L == -1:       
        return True

    if mapa[L][C] == "V":
        copia[L][C] = 'X'
        R = busca(mapa,L + 1,C)
        if R:
            return R
        R = busca(mapa,L -1,C)
        if R:
            return R
       
    elif mapa[L][C] == "H":
        copia[L][C] = 'X'
        R = busca(mapa,L,C + 1)
        if R:
            return R
        R = busca(mapa,L,C - 1)
        if R:
            return R
      
    elif mapa[L][C] == "T":
        copia[L][C] = 'X'
        R = busca(mapa,L,C + 1)
        if R:
            return R
        R = busca(mapa,L,C - 1)
        if R:
            return R  
        R = busca(mapa,L + 1,C)
        if R:
            return R
        R = busca(mapa,L -1,C)
        if R:
            return R               
    
    elif mapa[L][C] == "N":
        copia[L][C] = 'X'
        return False
               
for i in range(n):
    L, C = input().split()
    lista1.append(int(L))
    lista2.append(int(C))

for i in range(n):
    copia = [m.copy() for m in mapa]
    if busca(copia, lista1[i], lista2[i]):
        print("Fuga da cidade realizada.")
    else:
        print("Resgate aereo solicitado.")    
    