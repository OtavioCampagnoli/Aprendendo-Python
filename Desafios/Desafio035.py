#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

retaA = float(input('Informe o valor do primeiro lado: '))
retaB = float(input('Informe o valor do segundo lado: '))
retaC = float(input("Informe o valo do terceiro lado: "))
somaAB = retaA + retaB
somaBC = retaB + retaA

if somaAB > retaC or somaBC > retaA:
    print(f'Um TRIÂNGULO foi FORMADO... {somaAB}')
else:
    print(f'Impossível ser formar um triângulo')

# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

a = float(input('Informe o valor da reta A'))
b = float(input('Informe o valor da reta B'))
c = float(input('Informe o valor da reta C'))


if a + b > c and c + b > a:
    print('É triângulo.')
else:
    print('Não é triângulo.')