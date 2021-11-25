nome = str(input('Qual é o seu nome? '))
print(f'Prazer em te conhecer {nome:=<20}'.upper())
print(f'Prazer em te conhecer {nome:=^20}'.upper())
print(f'Prazer em te conhecer {nome:=>20}'.upper())

n1 = float(input('Um valor:'))
n2 = float(input('Outro valor: '))
s: float = n1 + n2
m: float = n1 * n2
d: float = n1 / n2
p: float = n1 ** n2
di: float = n1 // n2
restodiv: float = n1 % n2
print(f'A soma é: {s}\nA multiplicação é: {m}\nA Divisão é {d:.2f}\nA potenciação é:\nA divisão inteira é: {di}\nResto da divisão é:{restodiv}')