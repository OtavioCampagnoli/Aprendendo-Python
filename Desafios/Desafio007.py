#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

n1 = float(input('Informe a 1° nota'))
n2 = float(input('Informe a 2° nota'))
soma: float = n1 + n2
media: float = soma / 2
print(f'A média de {soma} é {media}')