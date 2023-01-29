veiculos = ['avião','carro','navio','ônibus']

f_maiuscula = lambda x: str.upper(x)

nome_maiusculos = list(map(f_maiuscula,veiculos))
print(nome_maiusculos)