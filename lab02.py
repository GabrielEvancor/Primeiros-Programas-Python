###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 2 - Fórmula 1
# Nome: Gabriel Evangelista Correia  
# RA: 250320
###################################################


t = float(input())
dist_a = int(input()) 	
vel_a = float(input()) 
t_pit_stop = float(input())
dist_b = int(input())
vel_b = float(input())
if (dist_a/vel_a)*3.6 + t_pit_stop + (dist_b/vel_b)*3.6 < t:
	print("True")
else:
	print("False")






