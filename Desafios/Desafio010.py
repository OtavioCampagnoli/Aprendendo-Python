#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar
# Cotação do dia 25/11/2021 $5.56.

real = float(input('Informe a quantidade de dinheiro que você tem na carteira:'))
conversaoDolar: float = real / 5.56
print(f'O valor de R${real:.2f} convertido em dólar é ${conversaoDolar:.2f}')