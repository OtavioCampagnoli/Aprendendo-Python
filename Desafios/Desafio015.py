# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. 
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

qtdeKmPercorrida = float(input('Informe a quantide de Kilômetros rodados:'  ))
qtdeDias = int(input('Informe a quantidade de dias em que o carro foi alugado:'))
precoPagar = qtdeDias * 60 + qtdeKmPercorrida * 0.15
print(f'O preço a pagar pelos {qtdeKmPercorrida}Km rodados, durante {qtdeDias} dias foi: R${precoPagar:.2f}')
