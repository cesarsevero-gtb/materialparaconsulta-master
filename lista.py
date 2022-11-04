'''
idade = [18, 20, 58, 30, 39]
posição  0   1   2   3   4

append adiciona no final da lista o valor
idade = [18, 20, 58, 30, 39]
idade.append(80)
print(idade)

insert(0, 'x') insere na posição desejada pode ser numero ou string
idade = [18, 20, 58, 30, 39]
#verifica se essa posição existe se não existir por padrão ele coloca no final
idade.insert(3, 10)
print(idade)

pop(1) remove o item da posição ou indice informada
idade = [18, 20, 58, 30, 39]
print(idade)
idade.pop(2)
print(idade)

remove('x') remove pelo valor informado # verificar se o valor existe
idade = [18, 20, 58, 30, 39]
print(idade)
idade.remove(58)
print(idade)

len() verifica quantas idades tem
idade = [18, 20, 58, 30, 39]
print(len(idade))

sort() organiza por ordem crescente
idade = [18, 20, 58, 30, 39]
idade.sort()
print(idade)

reverse organiza por ordem decrescente
idade = [18, 20, 58, 30, 39]
idade.sort(reverse = True)
print(idade)

reverse pode ser usado para reverte as posições
idade = [18, 20, 58, 30, 39]
idade.reverse()
print(idade)


max() acha o valor maximo da lista
idade = [18, 20, 58, 30, 39]
print(max(idade))

min() acha o valor minimo da lista
idade = [18, 20, 58, 30, 39]
print(min(idade))

sum() soma todo valor da lista
idade = [18, 20, 58, 30, 39]
print(sum(idade))
'''

idade = [18, 20, 58, 30, 39]
print(sum(idade))


