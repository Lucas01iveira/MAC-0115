'''E dito que uma matriz quadrada inteira é um quadrado mágico se a soma dos elementos de cada linha,
 a soma dos elementos de cada coluna e a soma dos elementos das diagonais principal e secundária são todas iguais.'''

def le_matriz():
    a = int(input('Entre com a quantidade de linhas/colunas da sua matriz: '))
    return cria_matriz(a)

def cria_matriz(x):
    n = []
    for i in range(x):
        linha = []
        for j in range(x):
            elemento = int(input('Entre com o elemento [{}][{}] da matriz: '.format(i+1,j+1)))
            linha.append(elemento)
        n.append(linha)
    return n

def apresenta_matriz(y):
    for i in range(len(y)):
        for j in range(len(y[0])):
            print('[{:^5}]'.format(y[i][j]),end='')
        print()

def quadrado_magico(m):
    n = True
    t = len(m)

    #verifico o valor da soma dos elementos na diagonal principal
    valor = 0
    for i in range(t):
        valor += m[i][i]

    #verifico a soma dos elementos da diagonal secundaria
    soma = 0
    for i in range(t):
        soma += m[i][(t-1)-i]
    if soma != valor:
        n = False

    #verifico, em cada linha, o valor da soma dos elementos
    for i in range(t):
        soma = 0
        for j in range(t):
            soma += m[i][j]
        if soma != valor:
            n = False

    #verifico, em cada coluna, o valor da soma dos elementos
    for j in range(t):
        soma = 0
        for i in range(t):
            soma += m[i][j]
        if soma!= valor:
            n = False
    return n

def main ():
    M = le_matriz()
    eh_magico = quadrado_magico(M)
    print ('='*25)
    if eh_magico:
        print ('A matriz: ')
        apresenta_matriz(M)
        print ('Eh um quadrado magico')
    else:
        print ('A matriz: ')
        apresenta_matriz(M)
        print ('Nao eh um quadrado magico')
main()