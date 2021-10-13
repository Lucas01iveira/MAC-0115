def le_matriz():
    lin = int(input('Digite a quantidade de linhas da sua matriz: '))
    col = int(input('Digite a quantidade de colunas da sua matriz: '))
    return cria_matriz (lin,col)

def cria_matriz (a,b):
    matriz = []
    for i in range (a):
        linha = []
        for j in range (b):
            a_ij = int(input(f'Entre com o elemento [{i+1}][{j+1}] da matriz: '))
            linha.append(a_ij)
        matriz.append(linha)
    return matriz

def apresenta (M):
    for i in range (len(M)):
        for j in range (len(M[0])):
            print('[{:^5}]'.format(M[i][j]), end='')
        print()

#Considerando que as duas matrizes inseridas na função sejam "multiplicáveis"
def produto (A,B):
    resultado = []
    for i in range (len(A)):
        linha = []
        for j in range (len(B[0])):
            elemento = 0
            for k in range (len(A[0])):
                elemento += A[i][k]*B[k][j]
            linha.append(elemento)
        resultado.append(linha)
    return resultado

def main():
    M = le_matriz()
    print('='*20)
    N = le_matriz()
    print('='*20)
    C = produto(M,N)

    print ('O produto entre essa matriz: ')
    apresenta(M)
    print()

    print ('E essa:')
    apresenta(N)
    print()

    print ('Resulta: ')
    apresenta(C)
main ()