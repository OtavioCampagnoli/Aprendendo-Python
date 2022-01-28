##3º Exercício
# Faça um programa em Python que leia um valor inteiro e mostre a tabuada de 1 a 10 do valor lido.
from ast import For


print('-----Tabuada-----')
n = int(input('Informe o número para ver a tabuada do respectivo número:'))
print(f'\n Tabuada de {n}:')

for i in range(1, 11):
   # print(n,'X', i, '=', (n * i))

    print(f'{n} X {i} = {n*i}')

    
    ## O for é utilizado para percorrer um valor dentro de um alcançe determinado! 
    # (O famoso contador) ele vai contar o valor da variavel ou constante!
