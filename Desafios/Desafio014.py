# Crie um algoritmo que receba uma temperatura em C°(Celsius)
# e converta essa temperatura para F°(Fahrenheit) e K (Kelvin)

temperaturaC = float(input('Informe a temperatura em C°'))
temperaturaF: float = temperaturaC * 9 / 5 + 32
temperaturaK: float = temperaturaC + 273.15
print(f'A temperatura em Celsius é {temperaturaC:.2f}C°\nA temperatura em Fahrenheit é '
f'{temperaturaF:.2f}F°\nA temperatura em Kevin é {temperaturaK:.2f}K')

