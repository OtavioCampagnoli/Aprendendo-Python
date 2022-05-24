#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

n1 = float(input('Informe o primeiro número: '))
n2 = float(input('Informe o segundo número: '))
n3 = float(input('Informe o terceiro número: '))
print(f'\nNúmeros informados: Primeiro: {n1:.2f}, Segundo: {n2:.2f}, Terceiro: {n3:.2f}')
#Verificando quem é menor:
if n2<n1 and n2<n3:
    menor = n2
if n3<n1 and n3<n2:
    menor = n3
if n1<n2 and n1<n3:
    menor = n1
# Verificando quem é maior:
if n1>n2 and n1>n3:
    maior = n1
if n2>n1 and n2>n3:
    maior = n2
if n3>n1 and n3>n2:
    maior = n3

print(f'O maior valor é: {maior}')
print(f'O menor valor é: {menor}')
