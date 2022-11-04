'''
try tratamento igual if mais é para tratamento
perto do try tem que ter um except

else opcional

finally idependete do que aconteça executará sempre esse comando

'''

try:
    x = int(input('Digite sua idade'))

except:
    print('você não digitou sua idade')
else:
    print(f'Sua idade é {x} anos')
finally:
    print('Muito obrigado por acessar')