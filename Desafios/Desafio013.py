# Faça um algoritmo que lei o salário de um funcionário e mostre o seu novo salário, com desconto de 15% de aumento.
nomeF = str(input('Informe o novo do funcionário: (Nome completo)'))
salario = float(input('Informe o seu sálario: (R$)'))

conta: float = salario + (salario * 15/100) # ou salario + (salario * 0.15)

print(f'O novo salário do funcionário {nomeF.upper()} com acréscimo de 15% é {conta:.2f}.')