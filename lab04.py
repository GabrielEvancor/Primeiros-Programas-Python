###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 4 - Avatar
# Nome:Gabriel Evangelista Correia 
# RA:250320
###################################################

W = 0.0
F = 0.0
E = 0.0
A = 0.0
X = 0.0
elemento = str(input())
while elemento != "X":
    P = float(input())
    if elemento == "W":
        W = W + P
        if F - P/2 > 0:
            F = F - P/2
        else:
            F = 0.0
    if elemento == "F":
        F = F + P
        if W - P/2 > 0:
            W = W - P/2
        else:
            W = 0.0
    if elemento == "E":
        E = E + P
        if A - P/2 > 0:
            A = A - P/2
        else:
            A = 0.0
    if elemento == "A":
        A = A + P
        if E - P/2 > 0:
            E = E - P/2
        else:
            E = 0.0
    elemento = input()

print("Pontuacao Final")
print("Agua:",W)
print("Terra:",E)
print("Fogo:",F)
print("Ar:",A)
if not((W == 0) or (F == 0) or (E == 0) or (A == 0)):
    print("Treinamento realizado com sucesso.")
if W == 0 or F == 0 or E == 0 or A == 0:
    print("Realize mais treinamentos.")