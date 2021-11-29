###
# Exercício Python 022: Crie um programa que leia o nome completo de uma pessoa e mostre:
#- O nome com todas as letras maiúsculas e minúsculas.
#- Quantas letras ao todo (sem considerar espaços).
#- Quantas letras tem o primeiro nome. ###

nome = str(input('Informe o seu nome completo:')).strip()
print('Analisando seu nome...')
print(f'O nome completo com todas as letras maiúsculas é {nome.upper()} \nO nome completo com todas as letras minúsculas é {nome.lower()}.')
print(f'Seu nome tem ao todo {len(nome) - nome.count(" ")} letras.')
print(f'O primeiro nome tem {nome.find(" ")} letras.')
