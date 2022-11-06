'''
importando bliblioteca do MsqL

fazendo os parametros

****************************
cursor = conexao.cursor()

cursor.execute('create table pessoas(nome varchar(30), idade int, endereco varchar(100));')

cursor.close()
conexao.close()


***************************************************
import pymysql.cursors
conexao = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    db='interacaopython',
    charset='utf8mb4',
    cursorclass= pymysql.cursors.DictCursor
)

criando tabela por aqui
with conexao.cursor() as cursor:
    cursor.execute('create table teste(nome varchar(30));')
    conexao.commit()

*****************************************
inserindo valor dentro do banco de dados via usuário
x = input('digite seu nome')
print(f'nome {x} adicionando ao banco de dados')

with conexao.cursor() as cursor:
    cursor.execute('insert into teste values("{}");'.format(x))
    conexao.commit()

**********************
adicionando uma tabela auto incremente
with conexao.cursor() as cursor:
    cursor.execute('create table cadastro(id int primary key auto_increment, nome varchar(30) not null, endereco varchar(100));')
    conexao.commit()

***********************************
adicionando mais de um valor na tabela
x = input('digite seu nome')
y = input('digite seu endereço')
print('Valores adicionado ao banco de dados')

with conexao.cursor() as cursor:
    cursor.execute('insert into cadastro(nome, endereco) values ("{}","{}");'.format(x, y))
    conexao.commit() #salva o que foi inserido

'''
import pymysql.cursors
conexao = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    db='interacaopython',
    charset='utf8mb4',
    cursorclass= pymysql.cursors.DictCursor
)

x = input('digite seu nome')
y = input('digite seu endereço')
print('Valores adicionado ao banco de dados')

with conexao.cursor() as cursor:
    cursor.execute('insert into cadastro(nome, endereco) values ("{}","{}");'.format(x, y))
    conexao.commit()