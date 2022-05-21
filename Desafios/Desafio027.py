#Exercício Python 027: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

n = str(input('Informe seu nome completo: ')).strip()
nome = n.split() # Quando eu sou split ele pega e divide a a variavel em listas ['Otavio', 'Henrique']
print(f'Seu primeiro nome é: {nome[0]} e seu último nome é {nome[len(nome) - 1]}')
