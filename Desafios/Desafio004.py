# Faca um programa que leia algo pelo teclado e mostre na tela o seu tipo
# primitivo e todas as informacoes possiveis sobre ele.

msg = input('Digite alguma coisa: ')

print(msg)
print('É numérico? ', msg.isnumeric())
print('É alfanumérico? ', msg.isalnum())
print('O tipo primitivo desse valor é:', type(msg))
print('Só tem espaços?', msg.isspace())
print('É alfabético?', msg.isalpha())
print('Está em maiusculas?', msg.isupper())
print('Está em minúsculas?', msg.islower())
print('Está capitalizado?', msg.istitle())

