#Faça um programa que leia a largura e a altura de uma parede em metros, calcule  a sua área e a quantidade de tinta
# necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m.

#declarando e recebendo os dados (Entrada de Dados)
altura = float(input('Informe a altura (metros):'))
largura = float(input('Informe a largura da parede (metros):'))

#processamento (Processamento de Dados)
area: float = altura*largura
tinta: float = area / 2

#retornando o processamento (Saída de Dados
print(f'Sua parede tem dimensão de {largura:.2f}X{altura:.2f} e sua área mede {area:.2f}m2.')
print(f'Para pintar a sua parede sera necessário {tinta:.2f}L de tinta.')