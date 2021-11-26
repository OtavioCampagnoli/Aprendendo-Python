# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira
# Ex: Digite um número: 6.127
# O número 6.127 tem a parte Inteira 6.
import math
#math.trunc(x)
#Retorna o valor x Real truncado com um Integral (geralmente um inteiro). Delega para x.__trunc__().
num = float(input('Informe qualquer valor:'))
print(f'O número {num} tem a parte Inteira {math.trunc(num)}.')