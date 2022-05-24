#Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

#Tem que ser divisível por 4, caso seja deve verificar se é divisível por 100;Caso não seja divisível por 4, verificar se o ano é divisível por 400; 
from datetime import date
ano = int(input('Qual ano deseja analisar? Digite 0 para analisar o ano atual...'))
if ano == 0:
    ano = date.today().year # método para pegar a data atual no caso o parametro do ano foi passado...
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano de {ano} é BISSEXTO!')
else:
    print(f'O ano de {ano} NÃO É BISSEXTO...')
