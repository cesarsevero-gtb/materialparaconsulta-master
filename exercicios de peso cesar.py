'''
faça um programa que receba o peso de 7 pessoas . calcule e mostre

*quantidade de pessoas acima de 90k
* a média dos pessos das pessoas

list.append(x)
Adiciona um item ao fim da lista. Equivalente a a[len(a):] = [x].

'''
x=[]
contador = 0
for i in range(0,7):
    x.append(float(input('digite seu peso')))
    if x[i] > 90:
        contador +=1



print(f'existem {contador} pessoas acima de 90KG e a media de todos os pesos é {sum(x)/len(x):.2f}')


