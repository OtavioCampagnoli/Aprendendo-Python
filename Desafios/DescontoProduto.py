#Crie um programa que calcule determinado(Qualquer valor) desconto,
# e aplique esse desconto no final da comprar daquele usuario

#Entrada de Dados
nomeC = str(input('Seja Bem-Vindo!\nInfome seu nome completo, por favor.')).upper()
nomeProduto = str(input('Informe o nome do produto: ')).upper()
valorP = float(input('Informe o valor do produto: R$'))
valorDesconto = float(input('Informe o valor do desconto: Por exemplo 10% ou 15%'))

#Processamento de dados

desconto = valorP - valorP * (valorDesconto / 100)

# Saída de Dados

print(f'Nome do cliente: {nomeC}\nNome do Produto: {nomeProduto}\nValor do Produto: {valorP:.2f}\nValor do desconto aplicado: {valorDesconto:.2f}\nValor Final: {desconto:.2f}')