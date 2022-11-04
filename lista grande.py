'''
x = [1, 2, 3, 4, 5, 6, 7]

print(x)

y = int(input('Digite o valor que deseja remover'))

if y in x:
    x.remove(y)
    print('O valor foi removido com sucesso')
    print(x)
else:
    print('Digitou um numero que não esta na lista ')

consultando por indice
x = [['cesar', 33], ['kelly', 34], ['Bolsonaro', 45], ['judite', 50]]

indice = int(input('qual indice quer consultar?'))

print(x[indice])

'''



x = [['cesar', 33], ['kelly', 34], ['Bolsonaro', 45], ['judite', 50]]

indice = int(input('qual indice quer consultar?'))

print(x[indice])



