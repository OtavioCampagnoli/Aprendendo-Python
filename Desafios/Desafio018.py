#Faça um programa que leia um ângulo qualquer e mostre na tela
# o valor do seno, cosseno e tangente desse ângulo

from math import radians, sin, cos, tan
angulo = float(input('Digite o ângulo que você deseja:'))
seno: float = sin(radians(angulo))
cosseno: float = cos(radians(angulo))
tangente: float = tan(radians(angulo))
print(f'O ângulo de {angulo}° tem o SENO de {seno:.2f}°')
print(f'O ângulo de {angulo}° tem o COSSENO de {cosseno:.2f}°')
print(f'O ângulo de {angulo}° tem a TANGENTE de {tangente:.2f}°')