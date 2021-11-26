# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos do alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
import random
al1 = str(input('Informe o nome 1° do aluno:'))
al2 = str(input('Informe o nome 2° do aluno:'))
al3 = str(input('Informe o nome 3° do aluno:'))
al4 = str(input('Informe o nome 4° do aluno:'))
lista = [al1, al2, al3, al4]
random.shuffle(lista)
print('A order da apresentação do trabalho será:')
print(lista)