'''
upper() transforma em maiusculo
str = 'cesar severo dos santos'
str = str.upper()
print(str)


lower() transforma em minusculo
str = 'CESAR SEVERO DOS SANTOS'
str = str.lower()
print(str)

replace('str', 'str') substitui a palavra por outra
str = 'cesar santos'
str = str.replace('santos', 'gostoso')
print(str)

caunt('str') conta quantas letras tem
str = 'aaf bbf ccf ddf ee f'
print(str.count('f'))


find('str')procura onde esta a palavras
str = ' cesar comeu o bolo da kelly'
print(str.find('bolo'))

printa a frase desejada
frase = 'Curso em Video Python'
print(frase[9:19])

lean() informa o comprimento da frase
frase = 'Curso em Video Python'
print(len(frase))

capitalize() deixa só a primeira letra maiuscula
frase = 'Curso em Video Python'
print(frase.capitalize())

title() tranforma a primeira letra em minuscula
frase = 'Curso em Video Python'
print(frase.title())

strip() remove os espaços inseridos desnecessarios
frase = '   Curso em Video Python   '
print(frase.strip())

rstrip()remove só os espaçoes da direita
frase = '   Curso em Video Python   '
print(frase.strip())

lstrip() remove só os espaçoes da esquerda
frase = '   Curso em Video Python   '
print(frase.strip())

split() separa as palavras
frase = 'Curso em Video Python'
print(frase.split())

''.join() irá separar as letras inserindo o que está dentro do ''
frase = 'Curso em Video Python'
print('-'.join(frase))

in verifica se a palavra extra na frase variavel boleana
frase = 'Curso em Video Python'
print('Video' in frase)

'''








