'''
modificando arquivos automaticamente

comando para abrir e criar caso não haja arquivo
arquivo = open('aulaPython.txt','w')

comando para fechar aquivo
arquivo.close()

comandos
'w' escrever ou alterar
'a' adicionar
'r' ler o arquivo

'''

arquivo = open('aulaPython.txt','a')

texto = '''
to aprendendo gostoso
sobre python
'''

arquivo.write(texto)

arquivo.close()