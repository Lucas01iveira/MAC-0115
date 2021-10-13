#não que esteja errado, mas aqui foi metido aquele miguezão
def main():
    n = str(input('Digite um numero: '))
    cont = len(n)
    n = aux = int(n)
    inverso = 0
    while aux != 0:
        inverso += (aux%10)*10**(cont-1)
        aux = aux//10
        cont -= 1
    print('O inverso de {} é {}'.format(n,inverso))
    if n == inverso:
        print('O número informado é palíndrome')
    else:
        print('O numero informado não é palíndrome')
main()