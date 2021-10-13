#esse algoritmo funciona para qualquer sequencia
def selecao_direta (seq):
    for i in range (len(seq)-1):
        for j in range (i+1,len(seq)):
            if seq[i] > seq[j]:
                #há algumas formas de realizar essa troca; utilizo o método clássico:
                aux = seq[j]
                seq[j] = seq[i]
                seq[i] = aux
    return seq

def cria_seq (x):
    cont = 1
    aux = []
    while cont <= x:
        num = int(input('Digite o {}o elemento: '.format(cont)))
        aux.append(num)
        cont += 1
    return aux

def main ():
    n = int(input('Quantos valores possuem a sua sequência de números? '))
    lista = cria_seq(n)
    print ('A sequencia informada foi: \n {} '.format(lista))
    print ('Devidamente ordenada, sua representação é a seguinte: \n {}'.format (selecao_direta(lista)))
main()