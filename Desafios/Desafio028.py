#Escreva um programa que faça o computador "pensar" em número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint 
from time import sleep
computador = randint(0, 5) # faz o computador sortear entre 0 - 5
print('')
print('-=-' * 20)
print('Irei pensar em entre 0 e 5.')
print('-=-' * 20)
jogador = int(input('Em qual número eu pensei?')) # JOGADOR TENTA ADIVINHAR
print('PROCESSANDO...')
sleep(1.5)
if(jogador == computador):
    print(f'Parabéns você acertou eu pensei em: {computador}.')
else:
    print(f'Poxa que pena foi quase... Eu tinha pensado em {computador}.')