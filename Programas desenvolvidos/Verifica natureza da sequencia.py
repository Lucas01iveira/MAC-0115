'''Dada uma sequencia de numeros inteiros, verificar se é crescente ou decresente'''

def main ():
    tot = int(input('Entre com a quantidade de elementos a serem inseridos na sequencia: '))
    crescente = True
    inicial = int(input('Entre com o 1o inteiro da sua sequencia: '))
    for i in range (1,tot):
        posterior = int(input('Entre com o {}o inteiro da sequencia: '.format(i+1)))
        if posterior < inicial:
            crescente = False
        inicial = posterior
    if crescente:
        print ('A sequencia de numeros inserida eh crescente')
    else:
        print ('A sequencia de numeros inserida nao eh crescente')
main ()
