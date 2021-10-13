'''Dizemos que uma matriz inteira Anxn  é uma matriz de permutação se em cada linha e em cada coluna
 houver n-1 elementos nulos e um único elemento igual a 1.'''

def le_matriz():
    a = int(input('Entre com a quantidade de linhas/colunas da matriz: '))
    return cria_matriz(a)

def cria_matriz(lin_col):
    m = []
    for i in range(lin_col):
        linha = []
        for j in range(lin_col):
            a_ij = int(input('Entre com o elemento [{}][{}] da matriz: '.format(i+1,j+1)))
            linha.append(a_ij)
        m.append(linha)
    return m

def apresenta (n):
    for i in range(len(n)):
        for j in range(len(n[0])):
            print('[{:^4}]'.format(n[i][j]), end='')
        print()

def verifica_permutacao (M):
    n = len(M)
    eh_permutacao = True

    # Verifico se as colunas estão organizadas conforme defnido no enunciado
    for j in range(n):
        zeros = 0
        um = 0
        for i in range(n):
            if M[i][j] == 0:
                zeros += 1
            else:
                if M[i][j] == 1:
                    um += 1
        if zeros != n - 1 or um != 1:
            eh_permutacao = False

    # Verifico se as linhas estão organizadas conforme definido no enunciado
    for i in range(n):
        zeros = 0
        um = 0
        for j in range(n):
            if M[i][j] == 0:
                zeros += 1
            else:
                if M[i][j] == 1:
                    um += 1
        if zeros != n - 1 or um != 1:
            eh_permutacao = False

    # Verifico se a diagonal principal está organizada conforme definido no enunciado
    zeros = 0
    um = 0
    for i in range(n):
        if M[i][i] == 0:
            zeros += 1
        else:
            if M[i][i] == 1:
                um += 1
    if zeros != n - 1 or um != 1:
        eh_permutacao = False

    # Verifico se a diagonal secundária está organizada conforme definido no enunciado
    zeros = 0
    um = 0
    for i in range(n):
        if M[i][(n-1) - i] == 0:
            zeros += 1
        else:
            if M[i][(n-1) - i] == 1:
                um += 1
    if zeros != n - 1 or um != 1:
        eh_permutacao = False

    return eh_permutacao

def main():
    M = le_matriz()
    resultado = verifica_permutacao(M)

    print('='*30 )
    if resultado == True:
        print('A matriz: ')
        apresenta(M)
        print('Eh matriz permutacao')
    else:
        print('A matriz: ')
        apresenta(M)
        print('Nao eh uma matriz permutacao')
main()

