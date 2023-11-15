###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 8 - Emparelhamento de Primers
# Nome:Gabriel Evangelista Correia
# RA: 250320
###################################################

DNA = str(input())
Primer = str(input())
lista = []
def inverter(Primer):
	return Primer[::-1]	

novo_primer = inverter(Primer)
n = len(novo_primer)
a = list(novo_primer)
a.remove(a[0])
a.remove(a[n-2])
novo_primer2 = "".join(a)
novo_primer2 = novo_primer2.replace("A",'t')
novo_primer2 = novo_primer2.replace("T",'a')
novo_primer2 = novo_primer2.replace("C",'g')
novo_primer2 = novo_primer2.replace("G",'c')
novo_primer2 = novo_primer2.upper()

if novo_primer2 in DNA:
    for i in range(len(DNA)): 
        lista.append(DNA.find(novo_primer2, i, i+len(novo_primer2)))
        if lista[i] != -1:
        	print("Ligacao na posicao" , lista[i])
else:
    print("Nenhuma ligacao")



