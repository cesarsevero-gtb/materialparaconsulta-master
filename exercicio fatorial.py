'''
faça um programa  que mostre o resultado de n!

resultado fatorial como funciona
5! = 5 * 4 * 3 * 2 * 1
8! = 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1

contador = 0
numeroFatorial = int(input('digite o numero fatorial'))

contador = numeroFatorial

for i in range(contador, 0):
    resultado  =  (numeroFatorial * contador)


print(resultado)

'''

x = int(input('digite o valor '))
fatorial = 1
for i in range(x, 0, -1 ):
    fatorial = fatorial * i

print(fatorial)





