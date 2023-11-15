###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 12 - Busca em Imagens
# Nome: Gabriel Evangelista correia 
# RA: 250320  
###################################################


P2 = input() 
m_matrizA, n_matrizA = [int(x) for x in input().split()]
_255 = input() 
matriz_A = []
for i in range(n_matrizA):
    linha = [int(x) for x in input().split()]
    matriz_A.append(linha)

P2_2 = input() 
m_matrizB, n_matrizB = [int(x) for x in input().split()]
_255_2 = input() 
matriz_B = []
for i in range(n_matrizB):
    linha = [int(x) for x in input().split()]
    matriz_B.append(linha)

def flip_horizontal(imagem_original, n_matrizB, m_matrizB):
    matriz_alterada = [a.copy() for a in imagem_original]
    for x in range(n_matrizB):
        for y in range(m_b):
            matriz_alterada[x][y] = imagem_original[i][m_b - 1 - j]
    return matriz_alterada
def flip_vertical(imagem_original, n_matrizB, m_matrizB):
    matriz_alterada = [a.copy for a in imagem_original]
    for x in range(n_matrizB):
        for y in range(m_b):
            matriz_alterada[x][y] = imagem_original[n_matrizB - 1 - i][j]
    return matriz_alterada

def rotacao_90(imagem_original):
    

def rotacao_180(imagem_original):






