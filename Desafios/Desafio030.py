#Crie um programa que leia um número inteiro e mostre se ele é PAR OU ÍMPAR.

numero = int(input('Informe um número para verificar se é PAR ou ÍMPAR'))

if(numero % 2 == 0):
    print(f'O número {numero} é PAR!')
else:
    print(f'O número {numero} é ÍMPAR!')