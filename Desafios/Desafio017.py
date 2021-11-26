#Faça um programa que leia o comprimento de cateto oposto e do cateto adjacente de um
# triângulo retângulo, calcule e mostre o comprimento da hipotenusa.
# Formula =  o quadro da hipotenusa é igual a soma dos quadrados dos catetos
import math
catetoMenor = float(input('Informe o valor do menor cateto.'))
catetoMaior = float(input('Informe o valor do maior cateto.'))
calcHipotenusa = math.sqrt(catetoMenor**2 + catetoMaior**2)
print(f'O valor da hipotenusa é: {calcHipotenusa:.5f}')