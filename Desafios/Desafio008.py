# Escreva um programa que lei um valor em metros e o exiba convertido em centímetros e milímetros.


valorM = float(input('Informe o valor em metros:'))
km: float = valorM / 1000
hm: float = km * 10
dam: float = valorM / 10
cent: float = valorM / 100
mm: float = cent / 100
hm: float = dam / 10
diametro: float = valorM * 10
print(f'O valor em kilômetros é: {km}Km \nO valor em hectômetro é: {hm}Hm\nO valor em decâmetro é: {dam}dam\nO Valor em metros é: {valorM}M\nO valor em centímetros é {cent}cm\nO valor em milímetros é {mm}mm')