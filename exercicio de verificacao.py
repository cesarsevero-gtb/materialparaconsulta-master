'''
faça um programa que verifica e mostre os numeros entre 1000 e 2000(inclusive)
que quando dividido por 11 produz resto igual a 5
'''

for i in range(1000, 2001):
    if i % 11 == 5:
        print(i)