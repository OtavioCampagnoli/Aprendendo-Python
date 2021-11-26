# Criar um algoritmo que receba um valor a ser investido e calcular de acordo com o tempo que queria investir (taxa a ser aplicada)

capital = float(input('Informe a quantide que queria investir:'))
i = float(input('Informe a taxa da aplicação (%)'))
nMeses = int(input('Informe quantos meses deseja investir (mês inteiro)'))
i = i / 100
m = capital * (1 + i) ** nMeses
print(f'O montante é R${m:.2f}')
