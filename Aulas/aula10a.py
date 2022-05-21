#Exemplo 01 
nome = str(input('Informe seu nome: ')).upper()
if nome == 'OTAVIO'or nome == 'OTÁVIO':
    print('Que nome lindo você tem!')
else:
    print('Seu nome é tão normal!')
print(f'Bom dia, {nome}')

#Exemplo 02 

n1 = float(input('Informe a sua primeira nota: '))
n2 = float(input('Informe a sua segunda nota: '))
m = (n1 + n2 ) / 2

print(f'A sua média foi: {m:.1f}')
if m >= 6.0:
    print('Sua média foi boa! PARABÉNS!')
else: 
    print('Sua média foi ruim! ESTUDE MAIS!')

#Exemplo 03
    nota1 = float(input('Informe a sua primeira nota: '))
    nota2 = float(input('Informe a sua segunda nota: '))
    media = (nota1 + nota2) / 2
    
    print('Aprovado!'if media >=6 else 'Estude mais!')