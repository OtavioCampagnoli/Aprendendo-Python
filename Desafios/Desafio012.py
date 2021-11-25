#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

pProduto = float(input('Informe o valor do produto (R$)'))

valorNovo = pProduto - (pProduto * 0.05)

print(f'O valor do produto com desconto de 5% é: R${valorNovo}')
