'''
declarando dicionario
x = {} ou x = dict{}

x = {'nome': 'cesar', 'idade': 33, 'telefone':'24229638' }
print(x) acessa toda a tabela
print(x['idade']) acessa apenas a tabela especifica

pop removendo um indidice informado
x = {'nome': 'cesar', 'idade': 33, 'telefone':'24229638' }
x.pop('idade')
print(x)

localizando um item dentro da lista ou a lista inteira
cadastro = [{'nome': 'cesar', 'idade': 33, 'telefone':'24229638' }, {'nome': 'kelly', 'idade': 34, 'telefone':'32229638' }]
print(cadastro[0]['telefone'])

'''

cadastro = [{'nome': 'cesar', 'idade': 33, 'telefone':'24229638' }, {'nome': 'kelly', 'idade': 34, 'telefone':'32229638' }]
print(cadastro[0]['telefone'])