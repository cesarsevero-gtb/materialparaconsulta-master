lista = [0,1,1,3,5,6,13,21,34,80]

f_numerospares = lambda x: x % 2 ==0

print(f_numerospares(5))

pares = list(filter(f_numerospares,lista))

print(pares)