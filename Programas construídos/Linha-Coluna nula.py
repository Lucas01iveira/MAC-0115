#Dada uma matriz  Amxn, imprimir o número de linhas e o número de colunas nulas da matriz.
def le_matriz():
    a = int(input('Digite a quantidade de linhas da sua matriz: '))
    b = int(input('Digite a quantidade de colunas da sua matriz: '))
    return cria_matriz(a,b)


def cria_matriz(lin,col):
    M = []
    for i in range(lin):
        linha = []
        for j in range(col):
            elemento = int(input('Digite o elemento [{}][{}]: '.format(i+1,j+1)))
            linha.append(elemento)
        M.append(linha)
    return M


def verifica_matriz(M):
    #defino uma variável indicadora de passagem para verificar se a matriz possui linha ou coluna nula
    #linhas:
    a = 0
    for i in range(len(M)):
        nula = True
        for j in range(len(M[0])):
            if M[i][j] != 0:
                nula = False
        if nula:
            a += 1

    #colunas:
    b = 0
    for j in range(len(M[0])):
        nula = True
        for i in range(len(M)):
            if M[i][j] != 0:
                nula = False
        if nula:
            b += 1

    return a,b


def apresenta_matriz(M):
    for i in range(len(M)):
        for j in range(len(M[0])):
            print('[{:^5}]'.format(M[i][j]),end='')
        print()


def main():
    A = le_matriz()
    print('=============================================\n')
    linhas_nulas, colunas_nulas = verifica_matriz(A)
    if linhas_nulas != 0 and colunas_nulas != 0:
        if linhas_nulas == 1:
            palavra_linhas = 'linha nula'
        else:
            palavra_linhas = 'linhas nulas'

        if colunas_nulas == 1:
            palavra_colunas = 'coluna nula'
        else:
            palavra_colunas = 'colunas nulas'

        print('A matriz: ')
        apresenta_matriz(A)
        print('possui {} {} e {} {}.'.format(linhas_nulas,palavra_linhas,colunas_nulas,palavra_colunas))

    elif linhas_nulas != 0 and colunas_nulas == 0:
        if linhas_nulas == 1:
            palavra_linhas = 'linha nula'
        else:
            palavra_linhas = 'linhas nulas'

        print('A matriz: ')
        apresenta_matriz(A)
        print('Não possui colunas nulas e possui {} {}.'.format(linhas_nulas,palavra_linhas))

    elif linhas_nulas == 0 and colunas_nulas != 0:
        if colunas_nulas == 1:
            palavra_colunas = 'coluna nula'
        else:
            palavra_colunas = 'colunas nulas'

        print('A matriz: ')
        apresenta_matriz(A)
        print('Não possui linhas nulas e possui {} {}.'.format(colunas_nulas,palavra_colunas))

    elif linhas_nulas == 0 and colunas_nulas == 0:
        print('A matriz: ')
        apresenta_matriz(A)
        print('Não possui linhas nem colunas nulas.')


main()