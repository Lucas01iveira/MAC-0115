# Nome: Lucas de Paula Oliveira
# Numero usp: 11222179
# Codigo da disciplina: MAC115
# Professor (a): Leliane

# Afirmo que este trabalho eh de minha autoria, fruto de meu trabalho individual, exceto onde eu
# reconhecer explicitamente o trabalho de outras pessoas.

# Defino a funcao modulo apenas por comodidade no tratamento posterior das demais funcoes
def modulo(x):
    if x > 0:
        return x
    return -x


def aproximaCOS(x, epsilon):
    j = 0
    # a variavel 'termo' representa o elemento que sera somado ao cosseno a cada repeticao do while
    termo = 1
    cos = 0
    while modulo(termo) >= epsilon:
        j = j + 1
        cos = cos + termo
        # a variavel 'coeficiente' representa o coeficiente responsavel por atualizar o valor do termo a cada repeticao do while
        coeficiente = (-1) * x * x / ((2 * j - 1) * (2 * j))
        termo = termo * coeficiente
    return cos, j


def integral_por_retangulos(k, epsilon, delta):
    n = 0
    integral = 0
    while n * delta <= k:
        # note que aqui o valor utilizado na fumcao aproximaCOS eh n*delta, que representa a altura da funcao
        # a cada pequeno retangulo aproximado
        cos, j = aproximaCOS(n * delta, epsilon)
        integral = integral + delta * cos
        n = n + 1
    # A funcao deve devolver o n-1, visto que o n 'atual' foi o que quebrou a condicao do while.
    return integral, j, n - 1


def aproximacao_suficiente(k, epsilon, delta, psi):
    primeiro, j, n = integral_por_retangulos(k, epsilon, delta)
    delta = delta / 2
    # Aqui m ja comeca com 1, visto que o intervalo delta ja foi dividido por 2 uma vez
    m = 1
    anterior, j, n = integral_por_retangulos(k, epsilon, delta)
    # Observe que foi necessario tomar dois valores iniciais de aproximacao de integral. Isso porque eh preciso ter um parametro inicial
    # da diferenca entre duas aproximacoes para que este possa ser comparado e atualizado posteriormente dentro do while.
    diferenca = modulo(primeiro - anterior)
    while diferenca > psi:
        delta = delta / 2
        integral, j, n = integral_por_retangulos(k, epsilon, delta)
        m = m + 1
        atual = integral
        diferenca = modulo(anterior - atual)
        anterior = atual
    return anterior, m, j, n


def main():
    k = float(input('Digite o valor do parametro k (limite de integracao): '))
    # Caso o usuario entre com o 0 no limite de integracao, nenhuma aproximacao deve ser feita. O resultado da integral eh zero
    if k == 0:
        print('O valor da integral eh 0')
    else:
        # Na condicao do if abaixo segue o valor de pi/2 com 5 casas decimais de precisao, caso o usuario entre com o valor limite para k
        if k == 1.57079:
            print('O valor da integral eh 1')
        else:
            # Faco a leitura dos parametros essenciais ao funcionamento do programa
            epsilon = float(input('Digite o valor de epsilon (erro maximo na funcao cos): '))
            delta = float(input('Digite o valor do parametro delta (tamanho maximo do intervalo de aproximacao): '))
            psi = float(input('Digite o valor do parametro psi (erro maximo na aproximacao da integral): '))
            # Apresento os resultados obtidos
            valor_integral, ordem_suficiente, ordem_taylor, numero_retangulo = aproximacao_suficiente(k, epsilon, delta,
                                                                                                      psi)
            print('O valor aproximado da integral eh {}'.format(valor_integral))
            print('Os valores que produziram essa aproximacao foram: ')
            print('m = {}, ou seja, intervalos de comprimento delta/(2^{})'.format(ordem_suficiente, ordem_suficiente))
            print('j = {}, ou seja, o cosseno foi expandido em Taylor ate ordem {}'.format(ordem_taylor, ordem_taylor))
            print('n = {} retangulos'.format(numero_retangulo))


main()


