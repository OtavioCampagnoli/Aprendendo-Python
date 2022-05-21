#Condicionais - Não esquecer de colocar o : apos a condicional
tempo = int(input('Quantos anos tem seu carro?'))
if tempo <=3:
    print('Carro novo')
else:
    print('Carro velho')
    
print('--FIM--')

#Condição simplicada     

tempo = int(input('Informe quantos anos tem seu carro?'))
print('carro novo' if tempo <=3 else 'carro velho')
print('--FIM--')


