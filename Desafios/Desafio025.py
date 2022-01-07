#Verificar uma String | Crie um prorama que leia o nome da uma pessoa de uma pessoa e diga se ela tem "SILVA" no nome
nome = str(input('Qual é seu nome completo?')).strip()
print('Seu nome tem Silva? {}'.format('SILVA' in  nome.upper()))
