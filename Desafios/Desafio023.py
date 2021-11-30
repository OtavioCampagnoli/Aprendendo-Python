# Faça um programa que leia um número de 0 a 9999 e mostre na tela ca um dos dígitos separados.

num = str(input('Informe um número de 0 a 9999:')).strip()
print(f'\nUnidade: {num[3]} \nDezena: {num[2]:>2} \nCentena: {num[3]}\nMilhar: {num[0]:>2}')