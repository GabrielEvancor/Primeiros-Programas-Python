###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 7 - Vacinação AstraZeneca
# Nome:Gabriel Evangelista Correia 
# RA:250320
###################################################

N = int(input())
D1 = []
D2 = [0,0,0]
X = []
vax = []

for i in range(N):
    vacinas_mes = int(input())
    vax.append(vacinas_mes)
if N == 3:
    for i in range(N):  
        D1.append(vax[i])
        X.append(0)
if 3<N<=6:
    for i in range(N-3):
        if vax[i] <= vax[i+3]:
            D1.append(int(vax[i]))
            X.append(0)
            D2.append(int(vax[i]))
        else:
            D1.append(int(vax[i+3]))
            X.append(int(vax[i]) - int(vax[i+3]))
            D2.append(int(vax[i+3]))
    for i in range(N-3, N):
        if i < 3: 
            X.append(0)
            D1.append(int(vax[i]))
        else:
            if vax[i] < vax[i-3]:
                D1.append(0)
                X.append(0)
            else:
                D1.append(int(vax[i]) - int(vax[i-3]))
                X.append(0)          
if N > 6:
    for i in range(N-3):
        if i-3 >= 0:
            if vax[i]>= D1[i-3]:
                if vax[i]-D1[i-3]>=vax[i+3]:
                    D1.append(int(vax[i+3]))
                    D2.append(int(vax[i+3]))
                    X.append(int(vax[i]) - (int(D1[i-3])) - (int(vax[i+3])))
                else:
                    X.append(0)
                    D2.append(int(vax[i])-int(D1[i-3]))
                    D1.append(int(vax[i])-int(D1[i-3]))
            else: 
                D1.append(0)
                X.append(0)
        else:
            if vax[i]>= vax[i+3]:
                X.append(int(vax[i]) - int(vax[i+3]))
                D1.append(int(vax[i+3]))
                D2.append(int(vax[i+3]))
            else:
                X.append(0) 
                D2.append(int(vax[i]))
                D1.append(int(vax[i]))        
    for i in range(N-3, N):
        if vax[i]>D1[i-3]:
            D1.append(int(vax[i])-int(D1[i-3]))
            X.append(0)
        else:
            D1.append(0)
            X.append(0)   
for i in range(N):
    print("Mes " + str(i+1) + ":")
    print("Vacinados com a primeira dose:", D1[i])
    print("Vacinados com a segunda dose:", D2[i])
    print("Vacinas devolvidas:", X[i])
SD1 = int(sum(D1)) - int(sum(D2))
SD2 = int(sum(D2))
SX = int(sum(X))
print("Total" + ":")
print("Vacinados apenas com a primeira dose:", SD1)
print("Vacinados com as duas doses:", SD2)
print("Vacinas devolvidas:", SX)