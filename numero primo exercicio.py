
textcaixa = int(input("Digite para saber se é primo o numero"))
def eh_primo(n):
    if(n<2):
     return False
    i=n//2
    while (i>1):
        if(n%i==0):
            return False
        i=i-1
    return True

def imprimir_resultado(numero, resultado):
    menssagem = f"O numero {numero} Não é Primo"
    if(resultado):
        menssagem =f"O numero {numero} é primo"
    return menssagem


numero = textcaixa
resultado=eh_primo(numero)
msg=imprimir_resultado(numero, resultado)
print(msg)
