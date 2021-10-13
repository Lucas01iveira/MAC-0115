def main():
    n = str(input('Digite um numero: '))
    inverso = n[::-1]
    print('O inverso do número inserido é igual a {}.'.format(inverso))
    if n == inverso:
        print('O número digitado é palíndrome!')
    else:
        print('O número digitado não é palíndrome!')
main()
