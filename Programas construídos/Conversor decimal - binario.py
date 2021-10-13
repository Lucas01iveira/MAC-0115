#dado um numero na base 10, o algoritmo o converte para a base binaria
def main():
    num = int(input('Digite um numero na base decimal: '))
    aux = num
    bin = 0
    cont = 0
    while aux != 0:
        bin += (aux%2)*(10**cont)
        aux = aux//2
        cont += 1
    print('O numero {} (base decimal) eh igual a {} (base binaria)'.format(num,bin))
main()