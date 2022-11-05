
#criando funcções
def mostrarnatela():
    print('Olá Mundo')
    print('Fim do Programa')

#mostrarnatela() chamando a função

def somarnumero(n1,n2):
    print(f'a soma dos numeros é {n1+n2}')
somarnumero(10, 20)

#cupla quando não sabemos a quantidade de paremetro vai ser inserida
def retornarCupla(*list):
    print(list)

retornarCupla(1, 2, 6, 9, 80, 96, 125, 30, 55)



def retornarCupla(*list):
    print(list)

retornarCupla(1, 2, 6, 9, 80, 96, 125, 30, 55)