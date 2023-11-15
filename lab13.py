###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 13 - Ordenação de Panquecas
# Nome:Gabriel Evangelista Correia 
# RA:250320
###################################################

pancakes = [int(x) for x in input().split()]
sorted_pancakes = sorted(pancakes)

def str_panquecas(lista):
    return(" ".join(map(str, lista)))

def indice_maximo(panqueca, relogio):
    maior_valor = len(panqueca) - relogio
    indice = max(panqueca[:maior_valor])
    return panqueca.index(indice)

def primeira_inversao(panqueca, relogio):
    posiçao_maior = indice_maximo(panqueca, relogio)
    aux_lista = panqueca[0:posiçao_maior + 1] 
    G = []
    if aux_lista != G:
        aux_lista.reverse()
        a = len(aux_lista)
        for i in range(a):
            panqueca[i] = aux_lista[i]
        E = aux_lista
        a = len(E)
        for i in range(a):
            panqueca[i] = E[i]
            return panqueca

def segunda_inversao(panqueca, relogio):
    aux_lista = panqueca[0:len(panqueca) - relogio]
    G = []
    if aux_lista != G:
        aux_lista.reverse()
        a = len(aux_lista)
        for i in range(a):
            panqueca[i] = aux_lista[i]
        E = aux_lista
        a = len(E)
        for i in range(a):
            panqueca[i] = E[i]
            return panqueca
if pancakes == sorted_pancakes:
    print("Panquecas ja ordenadas")
relogio = 0
while pancakes != sorted_pancakes:
    i_maior = indice_maximo(pancakes, relogio)
    if len(pancakes) - relogio - 1 == i_maior: #2 =
        relogio+=1
        continue
    else:
        print("Posicionando a panqueca", pancakes[i_maior])
        if i_maior != 0:
            print("Primeira inversao:", str_panquecas(primeira_inversao(pancakes, relogio)))
            coringa_2 = segunda_inversao(pancakes, relogio)
            print("Segunda inversao:", str_panquecas(coringa_2))
            relogio+=1
        else:
            coringa_2 = segunda_inversao(pancakes, relogio)
            print("Segunda inversao:", str_panquecas(coringa_2))
            relogio+=1