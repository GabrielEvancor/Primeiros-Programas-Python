######################################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 5 - Vacinação CoronaVac
# Nome:Gabriel Evangelista Correia 
# RA:250320
######################################################################

vacinas_disponiveis = 0
imunizadas_2doses = 0 #pessoas imunizadas com 2 doses
dose2_atrasada = 0 #pessoas que estão com a 2 dose atrasada D1A
Dose2_naoatrasada = 0 #pessoas que nao estao com a 2 dose atrasada D3
imunizadas_1dose = 0 #pessoas imunizadas com só 1 dose D1
segundadose_atraso = 0 #pessoas que tomaram 2 dose atrasada D2A
N = int(input())
for i in range(N):
    vacinas_disponiveis = int(input()) + vacinas_disponiveis
    if dose2_atrasada > 0:
        if dose2_atrasada < vacinas_disponiveis:
            vacinas_disponiveis = vacinas_disponiveis - dose2_atrasada
            imunizadas_2doses = imunizadas_2doses + dose2_atrasada
            segundadose_atraso = segundadose_atraso + dose2_atrasada
            dose2_atrasada = 0    
        else: 
            dose2_atrasada = dose2_atrasada - vacinas_disponiveis
            imunizadas_2doses = imunizadas_2doses + vacinas_disponiveis
            segundadose_atraso = segundadose_atraso + vacinas_disponiveis
            vacinas_disponiveis = 0
    else:
        if Dose2_naoatrasada > 0:
            if Dose2_naoatrasada < vacinas_disponiveis:
                vacinas_disponiveis = vacinas_disponiveis - Dose2_naoatrasada
                imunizadas_2doses = imunizadas_2doses + Dose2_naoatrasada
                Dose2_naoatrasada = 0
            else: 
                imunizadas_2doses = imunizadas_2doses + vacinas_disponiveis
                dose2_atrasada = Dose2_naoatrasada - vacinas_disponiveis
                vacinas_disponiveis = 0
                Dose2_naoatrasada = 0       
    Dose2_naoatrasada = vacinas_disponiveis
    imunizadas_1dose = Dose2_naoatrasada + dose2_atrasada
    vacinas_disponiveis = 0   
print("Pessoas completamente imunizadas:", imunizadas_2doses)
print("Pessoas imunizadas apenas com uma dose:", imunizadas_1dose)
print("Pessoas que tomaram a segunda dose com atraso:", segundadose_atraso)
print("Pessoas esperando a segunda dose com atraso:", dose2_atrasada)