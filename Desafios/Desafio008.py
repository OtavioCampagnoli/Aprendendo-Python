# Escreva um programa que lei um valor em metros e o exiba convertido em centímetros e milímetros.


valorM = float(input('Informe o valor em metros:'))
cent: float =  valorM / 100
mil: float = cent / 100
print(f'O Valor em metros é: {valorM}m\nO valor em centímetros é {cent}cm\nO valor em milímetros é {mil}mm')