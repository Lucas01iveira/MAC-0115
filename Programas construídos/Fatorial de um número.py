def fatorial(x):
    cont = x
    resultado = 1
    while cont > 0:
        resultado = cont*resultado
        cont -= 1
    return resultado

def main ():
    a = int(input('Digite um numero: '))
    print (f'O fatorial de {a} é igual a: {fatorial(a)}')
main()


