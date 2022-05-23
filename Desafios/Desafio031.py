#Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens até 200km e R$0,45 para viagens mais longas

from dis import dis


distancia = float(input('Informe a distãncia da viagem... (Km).'))
pViagem200KM = distancia * 0.50
pViagemMaior = distancia * 0.45
if(distancia <= 200):
    print(f'\nNa viagem de {distancia}Km.\nO preço da passagem é: R${pViagem200KM}')
else:
    print(f'\nNa viagem de {distancia}Km\nO preço da passagem é: R${pViagemMaior}')