#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar
# Cotação do dia 25/11/2021 $5.56.

v = float(input('Informe a quantidade de dinheiro que você tem na carteira'))
conversaoDolar: float = v / 5.56
print(f'O valor de R${v:.2f} convertido em dólar é ${conversaoDolar:.2f}')