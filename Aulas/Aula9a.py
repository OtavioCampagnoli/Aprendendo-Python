msg = str('curso em vídeo python')
print(msg[9::3]) # QUANDO SE COLOCA 9:ATE O FINAL DA STRING:3 ELE VAI COMECAR A PARTIR DO 9 OU SEJA V E VAI PULAR DE 3 EM TRES CASAS ATE O FINAL
print(len(msg)) # VAI IMPRIMIR O TAMANHO DA VARIAVEL MSG
print(msg.count('o')) # VAI CONTAR QUANTAS LETRAS TEM NA VARIAVEL MSG
print(msg.count('o', 0, 21)) # VAI CONTAR QUANTAS LETRAS TEM NA VARIAVEL MSG, PEGANDO DA PRIMEIRA POSICAO ATE A POSICAO 21
print(msg.find('deo'))
print(msg.find('Android')) # O VALOR -1 EH RETORNADO QUANDO A O METODO FIND() NAO ACHA O PARAMETRO INSERIDO ENTRE(NO CASO 'ANDROID')
print('Curso' in  msg)
print(msg.replace('Python', 'Android'))
print('Usando o upper():', msg.upper())
print('Usando o lower():', msg.lower())
print('Usando capitalize():', msg.capitalize()) # O CAPITALIZE IRA PEGAR TODA A STRING E COLOCAR A PRIMEIRA LETRA DELA EM MAIUSCULO
print(msg.title())
print(msg.strip().replace('curso', 'Aula'))
print(msg.rstrip())
print(msg.split())## Divisao
print('-'.join(msg.capitalize()))##Juncao