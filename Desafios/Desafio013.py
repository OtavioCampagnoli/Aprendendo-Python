# Faça um algoritmo que lai o salário de um funcionário e mostre o seu novo salário, com desconto de 15% de aumento.
nomeF = str(input('Informe o novo do funcionário: (Nome completo)'))
salario = float(input('Informe o seu sálario: (R$)'))

conta: float = salario + (salario * 0.15)

print(f'O novo salário do funcionário {nomeF} com acréscimo de 15% é {conta}.')