n1 = int(input('Digite um valor: '))#observacao colocar o tipo de dados, porque senao o python ira concatenar(pois ele ire achar que uma string)
n2 = int(input('Digite outro valor: '))
soma = n1 + n2
#print('A soma entre', n1, "e", n2 , 'vale', soma)
print(f'A soma entre {n1} e {n2} vale {soma}') #sintaxe nova com metodo .format()` ou colocar f antes das '' e colocar os parametros dentro das chaves!