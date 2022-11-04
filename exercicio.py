'''
Crie um sistema onde deve inserir nome e idade
e as media das provas
'''

nome = input('Digite seu nome completo:')
idade = int(input('Digite sua idade:'))

provap = int(input('Quanto tirou na prova de português? '))
provam = int(input('Quanto tirou na prova de matematica? '))

media = (provam + provap) / 2

nome = nome.title()

print('Nome do Aluno:',nome)
print('Idade:', idade)

if idade >= 18 and media >=6:
    print('{} passou de Ano'.format(nome))
else :
    print('{} Reprovado pois não cumpriu os requisitos'.format(nome))




