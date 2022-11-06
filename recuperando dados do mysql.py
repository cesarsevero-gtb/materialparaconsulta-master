'''
mostra a linha toda separada
with conexao.cursor() as cursor:
    cursor.execute('select * from cadastro')
    resultado = cursor.fetchall()

for dado in resultado:
    print(dado)

mostra apenas uma parte da lista exemplo nome
with conexao.cursor() as cursor:
    cursor.execute('select * from cadastro')
    resultado = cursor.fetchall()

for dado in resultado:
    print(dado['nome'])
'''
import pymysql.cursors

conexao = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    db='interacaopython',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor

)

with conexao.cursor() as cursor:
    cursor.execute('select * from cadastro')
    resultado = cursor.fetchall()

for dado in resultado:
    print(dado['nome'])