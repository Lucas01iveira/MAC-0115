def main():
    num = int(input('Digite um numero na base binaria: '))
    aux = num
    cont = 0
    dec = 0
    while aux != 0:
        dec += (aux%10)*(2**cont)
        aux = aux//10
        cont += 1
    print ('O numero {} (base binaria) eh igual a {} (base decimal)'.format(num,dec))
main()