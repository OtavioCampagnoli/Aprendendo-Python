#Faça um programa que leia uma frase pelo teclado e mostre:
# Quantas vezes aparece a letra "A".
# Em que posição ela aparece a primeira vez.
# Em que posição ela aparece a última vez.

#Entrada de Dados
frase = str(input('Informe uma frase: ')).upper().strip()
cont = frase.count('A')
calc = frase.find('A')
con = frase.rfind('A')
print(f'O nome tem {cont} A no total,\nO primeiro A aparece na {calc} posição, \nO último A aparece na {con} posição')




