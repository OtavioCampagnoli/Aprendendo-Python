#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.




salario = float(input('Informe o salário: R$'))

if salario > 1250:
    salario += salario * 0.10
    print(f'Parabéns você recebeu 10% de acréscimo\nSeu novo salário é: R${salario}')
else:
    salario += salario * 0.15
    print(f'Parabéns você recebeu 15% de acréscimo\nSeu novo salário é: R${salario}')
 