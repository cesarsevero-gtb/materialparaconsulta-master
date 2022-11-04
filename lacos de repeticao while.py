'''
condição de repetição
while tradução enquanto

Exemplo um
x = 0
while x < 10:
    print('1')
    x = x + 1

print('Você saiu do laço')
**********************************************************************************************
Onde usala exemplo 2
decisao = 0

while decisao !=3:
    decisao = int(input('Digite 1 para logar 2 para cadastrar e 3 para sair'))

    if decisao == 1:
        print('logando')
    elif decisao == 2:
        print('cadastrando')

print('Você saiu do laço')

**********************************************************************************************

break serve pra sair do laço também exemplo
decisao = 0

while True:
    decisao = int(input('Digite 1 para logar 2 para cadastrar e 3 para sair'))

    if decisao == 3:
        break

    if decisao == 1:
        print('logando')
    elif decisao == 2:
        print('cadastrando')

print('Você saiu do laço')

**************************************************
continue comando que não executa a linha desejada apenas continua
x = -1
while x < 11:
    x += 1
    if x == 5:
        continue

    print(x)

'''

x = -1
while x < 11:
    x += 1
    if x == 5:
        continue

    print(x)



