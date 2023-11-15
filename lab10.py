#####################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 10 - linha do Tempo Sagrada
# Nome: Gabriel Evangelista Correia 
# RA: 250320
#####################################################


matriz = []
for i in range(11):
    matriz.append(list(input()))        

ramo = [] 
nexus = []
instavel = [] 

for c in range(50):
    if matriz[6][c] == '+':
       ramo.append(c)
    if matriz[4][c] == '+':
       ramo.append(c)
ramo.sort()       

for i in range(len(ramo)):
    repetido1 = []
    line = 6
    row = ramo[i]
    if matriz[line][row] != ".":
        while True:
            if  matriz[line][row+1] == "+" and (line,row+1) not in repetido1:
                repetido1.append((line,row))
                row = row + 1

                if row == 49:
                    nexus.append(ramo[i])
                    break    

            elif  matriz[line][row-1] == "+" and (line,row-1) not in repetido1:
                repetido1.append((line,row))
                row = row - 1
                if row == 0:
                    nexus.append(ramo[i])
                    break

            elif matriz[line-1][row] == "+" and (line-1,row) not in repetido1:
                repetido1.append((line,row))
                line = line - 1
                
            elif matriz[line+1][row] == "+" and (line+1,row) not in repetido1:
                repetido1.append((line,row))
                line = line + 1
                if line == 10:
                    nexus.append(ramo[i])
                    break
            else:
                instavel.append(ramo[i])
                break                   
            

for i in range(len(ramo)):
    repetido = []
    line = 4
    row = ramo[i]
    if matriz[line][row] != ".":
        while True:
            if  matriz[line][row+1] == "+" and (line,row+1) not in repetido:
                repetido.append((line,row))
                row = row + 1
                if row == 49:
                    nexus.append(ramo[i])
                    break    

            elif  matriz[line][row-1] == "+" and (line,row-1) not in repetido:
                repetido.append((line,row))
                row = row - 1
                if row == 0:
                    nexus.append(ramo[i])
                    break
            elif matriz[line+1][row] == "+" and (line+1,row) not in repetido:
                repetido.append((line,row))
                line = line + 1    

            elif matriz[line-1][row] == "+" and (line-1,row) not in repetido:
                repetido.append((line,row))
                line = line - 1
                if line == 0:
                    nexus.append(ramo[i])
                    break 
            else:
                instavel.append(ramo[i])
                break               

for i in range(len(ramo)):
    if ramo[i] in nexus:
        print(f"Bifurcacao {ramo[i]}: Evento Nexus")
    else:
        print(f"Bifurcacao {ramo[i]}: Instavel")