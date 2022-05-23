#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi mutado. A multa vai custar R$7,00 por cada Km acima do limite.

from random import randint

velocidade = randint(0.00, 220.00) # Colocando a velocidade aleatória entre 0.0, 220.0
desconto = (velocidade - 80.00)
multa = 7.00 * desconto

if velocidade <= 80.00:
    print(f'Tudo certo por aqui! Dentro do limite... \nSua velocidade: {velocidade}Km/h')
else:
    print(f'Sua velocidade foi: {velocidade}Km/h\nVocê passou {desconto}Km/h a mais do limite de velocidade! Sua multa é: R${multa}.')