#####################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 14 - Linha do Tempo Sagrada II
# Nome:Gabriel Evangelista Correia 
# RA:250320
#####################################################


def eventos_nexus(matriz, linha, coluna):
    print("linha: ",linha,"coluna: ",coluna)
    if linha == 4 or linha == 6:
        pontos.append(coluna)
    else:
        if matriz[linha+1][coluna] == "+":
            return eventos_nexus(matriz, linha+1, coluna)
        if matriz[linha+1][coluna+1] == "+":
            return eventos_nexus(matriz, linha+1, coluna+1)
        if matriz[linha+1][coluna-1] == "+":
            return eventos_nexus(matriz, linha+1, coluna-1)
        if matriz[linha][coluna+1] == "+":
            return eventos_nexus(matriz, linha, coluna+1)
        if matriz[linha][coluna-1] == "+":
            return eventos_nexus(matriz, linha, coluna-1)
        if matriz[linha-1][coluna] == "+":
            return eventos_nexus(matriz, linha-1, coluna)
        if matriz[linha-1][coluna-1] == "+":
            return eventos_nexus(matriz, linha-1, coluna-1)
        if matriz[linha-1][coluna+1] == "+":
            return eventos_nexus(matriz, linha-1, coluna+1)
def eventos_nexus_baixo(matriz, linha, coluna):
    print("linha: ",linha,"coluna: ",coluna)
    if linha == 4 or linha == 6:
        pontos.append(coluna)
    else:
        if matriz[linha-1][coluna] == "+":
            return eventos_nexus_baixo(matriz, linha-1, coluna)
        if matriz[linha-1][coluna-1] == "+":
            return eventos_nexus_baixo(matriz, linha-1, coluna-1)
        if matriz[linha-1][coluna+1] == "+":
            return eventos_nexus_baixo(matriz, linha-1, coluna+1)
        if matriz[linha][coluna+1] == "+":
            return eventos_nexus_baixo(matriz, linha, coluna+1)
        if matriz[linha][coluna-1] == "+":
            return eventos_nexus_baixo(matriz, linha, coluna-1)
        if matriz[linha+1][coluna] == "+":
            return eventos_nexus_baixo(matriz, linha+1, coluna)
        if matriz[linha+1][coluna+1] == "+":
            return eventos_nexus_baixo(matriz, linha+1, coluna+1)
        if matriz[linha+1][coluna-1] == "+":
            return eventos_nexus_baixo(matriz, linha+1, coluna-1)

pontos = []
matriz = []
for i in range(11):
    matriz.append(list(input()))
for j in range(50):
    if matriz[0][j] == "+":
        eventos_nexus(matriz, 0, j)
for j in range(50):
    if matriz[10][j] == "+":
        eventos_nexus_baixo(matriz, 10, j)
print(pontos)
'''
print("Ramificacao {0}: {1} Eventos Nexus.".format(coluna, X))
'''