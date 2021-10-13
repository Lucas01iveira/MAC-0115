# ------------------------------------------------------------------
# Nome: Lucas de Paula Oliveira
# NUSP: 11222179
# Codigo da disciplina: MAC115
# EP3: Caca ao ouro no mundo do Wumpus
#
# Afirmo que esse trabalho eh de minha autoria, fruto de meu trabalho individual
# exceto onde eu reconhecer explicitamente o trabalho de outras pessoas
# ------------------------------------------------------------------
def le_mundo(arquivo):
    aux = []
    with open(arquivo, 'r', encoding='utf-8') as arq_entrada:
        for linha in arq_entrada:
            linha_sem_brancos = linha.strip()
            lista = linha_sem_brancos.split()
            aux.append(lista)

    M = []
    for k in range(int(aux[0][0])):
        M = M + [[0] * int(aux[0][0])]

    N = []
    for k in range(int(aux[0][0])):
        N = N + [['?'] * int(aux[0][0])]

    # Aqui basta esse indice p percorrer cada linha (ja sabemos o que cada uma significa)
    for i in range(1, len(aux)):
        M[int(aux[i][0])][int(aux[i][1])] = int(aux[i][2])

    return M, N


# passo tambem a matriz mundo_usuario para que ela possa ser impressa
def imprime_percepcao(percebe, agente, choque, urro):
    if choque:
        if percebe[agente[0]][agente[1]] == 0:
            print('Percepcao apos ultima acao: \n [C]')

        if percebe[agente[0]][agente[1]] == 100:
            print('Percepcao apos ultima acao: \n [F,C]')

        if percebe[agente[0]][agente[1]] == 10:
            print('Percepcao apos ultima acao: \n [B,C]')

        if percebe[agente[0]][agente[1]] == 1:
            if estado[2] == 1:
                print('Percepcao apos ultima acao: \n [R,C]')
            else:
                print('Percepcao apos ultima acao: \n [C]')

        if percebe[agente[0]][agente[1]] == 111:
            if estado[2] == 1:
                print('Percepcao apos ultima acao: \n [F,B,R,C]')
            else:
                print('Percepcao apos ultima acao: \n [F,B,C]')

        if percebe[agente[0]][agente[1]] == 110:
            print('Percepcao apos ultima acao: \n [F,B,C]')

        if percebe[agente[0]][agente[1]] == 101:
            if estado[2] == 1:
                print('Percepcao apos ultima acao: \n [F,R,C]')
            else:
                print('Percepcao apos ultima acao: \n [F,C]')

        if percebe[agente[0]][agente[1]] == 11:
            print('Percepcao apos ultima acao: \n [B,T,C]')

    else:
        # Se o wumpus foi morto apos a ultima jogada do usuario, entao apresento na tela a percepcao do urro. Basicamente sao as mesmas condicoes anteriores acrescidas de 'U'.
        if urro:
            if percebe[agente[0]][agente[1]] == 0:
                print('Percepcao apos ultima acao: \n [U]')

            if percebe[agente[0]][agente[1]] == 100:
                print('Percepcao apos ultima acao: \n [F,U]')

            if percebe[agente[0]][agente[1]] == 10:
                print('Percepcao apos ultima acao: \n [B,U]')

            if percebe[agente[0]][agente[1]] == 1:
                if estado[2] == 1:
                    print('Percepcao apos ultima acao: \n [R,U]')
                else:
                    print('Percepcao apos ultima acao: \n [U]')

            if percebe[agente[0]][agente[1]] == 111:
                if estado[2] == 1:
                    print('Percepcao apos ultima acao: \n [F,B,R,U]')
                else:
                    print('Percepcao apos ultima acao: \n [F,B,U]')

            if percebe[agente[0]][agente[1]] == 110:
                print('Percepcao apos ultima acao: \n [F,B,U]')

            if percebe[agente[0]][agente[1]] == 101:
                if estado[2] == 1:
                    print('Percepcao apos ultima acao: \n [F,R,U]')
                else:
                    print('Percepcao apos ultima acao: \n [F,U]')

            if percebe[agente[0]][agente[1]] == 11:
                print('Percepcao apos ultima acao: \n [B,R,U]')
        else:
            if percebe[agente[0]][agente[1]] == 0:
                print('Percepcao apos ultima acao: \n []')

            if percebe[agente[0]][agente[1]] == 100:
                print('Percepcao apos ultima acao: \n [F]')

            if percebe[agente[0]][agente[1]] == 10:
                print('Percepcao apos ultima acao: \n [B]')

            if percebe[agente[0]][agente[1]] == 1:
                if estado[2] == 1:
                    print('Percepcao apos ultima acao: \n [R]')
                else:
                    print('Percepcao apos ultima acao: \n []')

            if percebe[agente[0]][agente[1]] == 111:
                if estado[2] == 1:
                    print('Percepcao apos ultima acao: \n [F,B,R]')
                else:
                    print('Percepcao apos ultima acao: \n [F,B]')

            if percebe[agente[0]][agente[1]] == 110:
                print('Percepcao apos ultima acao: \n [F,B]')

            if percebe[agente[0]][agente[1]] == 101:
                if estado[2] == 1:
                    print('Percepcao apos ultima acao: \n [F,R]')
                else:
                    print('Percepcao apos ultima acao: \n [F]')

            if percebe[agente[0]][agente[1]] == 11:
                print('Percepcao apos ultima acao: \n [B,R]')

    mundo_usuario[agente[0]][agente[1]] = agente[2]
    print('Mundo do Wumpus conhecido pelo agente:')
    print('-' * (7 * len(mundo) + len(mundo) + 1))
    for i in range(len(mundo)):
        for k in range(len(mundo[0])):
            if k != (len(mundo) - 1):
                print('|{:^7}'.format(mundo_usuario[i][k]), end='')
            else:
                print('|{:^7}|'.format(mundo_usuario[i][k]))
        print('-' * (7 * len(mundo) + len(mundo) + 1))


def atualiza_percepcaoEagente(mundo, agente, estado, percebe, acao, choque, urro):
    if acao == 'M':
        # Registro a perda de -1 ponto
        estado[3] = estado[3] - 1
        # Antes do movimento ser contabilizado a orientacao do agente deve ser sempre verificada.
        if agente[2] == '^':
            # verifico se a casa para a qual o usuario quer se movimentar esta dentro do mundo. Caso nao esteja ocorre um choque,
            # caso esteja o movimento eh executado
            if agente[0] - 1 < 0:
                # percepcao de choque
                choque = True
            else:
                if percebe[agente[0]][agente[1]] == 0:
                    mundo_usuario[agente[0]][agente[1]] = ''
                else:
                    if percebe[agente[0]][agente[1]] == 10:
                        mundo_usuario[agente[0]][agente[1]] = 'B'
                    else:
                        if percebe[agente[0]][agente[1]] == 100:
                            mundo_usuario[agente[0]][agente[1]] = 'F'
                        else:
                            if percebe[agente[0]][agente[1]] == 110:
                                mundo_usuario[agente[0]][agente[1]] = 'FB'
                            else:
                                if percebe[agente[0]][agente[1]] == 1:
                                    mundo_usuario[agente[0]][agente[1]] = 'R'
                                else:
                                    if percebe[agente[0]][agente[1]] == 11:
                                        mundo_usuario[agente[0]][agente[1]] = 'BR'
                                    else:
                                        if percebe[agente[0]][agente[1]] == 111:
                                            mundo_usuario[agente[0]][agente[1]] = 'FBR'

                agente[0] = agente[0] - 1
                # Verifico se a sala para a qual o agente se movimentou contem um Wumpus ou um poco
                if mundo[agente[0]][agente[1]] == 1 or (mundo[agente[0]][agente[1]] == 2 and estado[0] == 1):
                    estado[3] = estado[3] - 1000000

        if agente[2] == 'v':
            if agente[0] + 1 >= len(mundo):
                # percepcao de choque
                choque = True
            else:
                if percebe[agente[0]][agente[1]] == 0:
                    mundo_usuario[agente[0]][agente[1]] = ''
                else:
                    if percebe[agente[0]][agente[1]] == 10:
                        mundo_usuario[agente[0]][agente[1]] = 'B'
                    else:
                        if percebe[agente[0]][agente[1]] == 100:
                            mundo_usuario[agente[0]][agente[1]] = 'F'
                        else:
                            if percebe[agente[0]][agente[1]] == 110:
                                mundo_usuario[agente[0]][agente[1]] = 'FB'
                            else:
                                if percebe[agente[0]][agente[1]] == 1:
                                    mundo_usuario[agente[0]][agente[1]] = 'R'
                                else:
                                    if percebe[agente[0]][agente[1]] == 11:
                                        mundo_usuario[agente[0]][agente[1]] = 'BR'
                                    else:
                                        if percebe[agente[0]][agente[1]] == 111:
                                            mundo_usuario[agente[0]][agente[1]] = 'FBR'

                agente[0] = agente[0] + 1
                # Verifico se a sala para a qual o agente se movimentou contem um Wumpus ou um poco
                if mundo[agente[0]][agente[1]] == 1 or (mundo[agente[0]][agente[1]] == 2 and estado[0] == 1):
                    estado[3] = estado[3] - 10000000

        if agente[2] == '>':
            if agente[1] + 1 >= len(mundo[0]):
                # percepcao de choque
                choque = True
            else:
                if percebe[agente[0]][agente[1]] == 0:
                    mundo_usuario[agente[0]][agente[1]] = ''
                else:
                    if percebe[agente[0]][agente[1]] == 10:
                        mundo_usuario[agente[0]][agente[1]] = 'B'
                    else:
                        if percebe[agente[0]][agente[1]] == 100:
                            mundo_usuario[agente[0]][agente[1]] = 'F'
                        else:
                            if percebe[agente[0]][agente[1]] == 110:
                                mundo_usuario[agente[0]][agente[1]] = 'FB'
                            else:
                                if percebe[agente[0]][agente[1]] == 1:
                                    mundo_usuario[agente[0]][agente[1]] = 'R'
                                else:
                                    if percebe[agente[0]][agente[1]] == 11:
                                        mundo_usuario[agente[0]][agente[1]] = 'BR'
                                    else:
                                        if percebe[agente[0]][agente[1]] == 111:
                                            mundo_usuario[agente[0]][agente[1]] = 'FBR'

                agente[1] = agente[1] + 1
                # Verifico se a sala para a qual o agente se movimentou contem um Wumpus ou um poco
                if mundo[agente[0]][agente[1]] == 1 or (mundo[agente[0]][agente[1]] == 2 and estado[0] == 1):
                    estado[3] = estado[3] - 10000000

        if agente[2] == '<':
            if agente[1] - 1 < 0:
                # percepcao de choque
                choque = True
            else:
                if percebe[agente[0]][agente[1]] == 0:
                    mundo_usuario[agente[0]][agente[1]] = ''
                else:
                    if percebe[agente[0]][agente[1]] == 10:
                        mundo_usuario[agente[0]][agente[1]] = 'B'
                    else:
                        if percebe[agente[0]][agente[1]] == 100:
                            mundo_usuario[agente[0]][agente[1]] = 'F'
                        else:
                            if percebe[agente[0]][agente[1]] == 110:
                                mundo_usuario[agente[0]][agente[1]] = 'FB'
                            else:
                                if percebe[agente[0]][agente[1]] == 1:
                                    mundo_usuario[agente[0]][agente[1]] = 'R'
                                else:
                                    if percebe[agente[0]][agente[1]] == 11:
                                        mundo_usuario[agente[0]][agente[1]] = 'BR'
                                    else:
                                        if percebe[agente[0]][agente[1]] == 111:
                                            mundo_usuario[agente[0]][agente[1]] = 'FBR'

                agente[1] = agente[1] - 1
                # Verifico se a sala para a qual o agente se movimentou contem um Wumpus ou um poco
                if mundo[agente[0]][agente[1]] == 1 or (mundo[agente[0]][agente[1]] == 2 and estado[0] == 1):
                    estado[3] = estado[3] - 1000000

    if acao == 'D':
        # Registro a perda de -1 ponto
        estado[3] = estado[3] - 1
        # Verifico a orientacao do agente para que a acao seja executada corretamente em cada caso
        if agente[2] == '^':
            agente[2] = '>'
        else:
            if agente[2] == '>':
                agente[2] = 'v'
            else:
                if agente[2] == 'v':
                    agente[2] = '<'
                else:
                    if agente[2] == '<':
                        agente[2] = '^'

    if acao == 'E':
        # registro a perda de -1 ponto
        estado[3] = estado[3] - 1
        # verifico a orientacao do agente para que a acao seja executada da maneira correta
        if agente[2] == '^':
            agente[2] = '<'
        else:
            if agente[2] == '<':
                agente[2] = 'v'
            else:
                if agente[2] == 'v':
                    agente[2] = '>'
                else:
                    if agente[2] == '>':
                        agente[2] = '^'

    if acao == 'T' and estado[1] == 1:
        # Registro a perda de -1 ponto e a perda da flecha
        estado[3] = estado[3] - 1
        estado[1] = estado[1] - 1
        if agente[2] == '^':
            # verifico se o Wumpus esta na sala para a qual o agente disparou a flecha
            for i in range(agente[0], 0, -1):
                if mundo[i][agente[1]] == 2 and estado[0] == 1:
                    estado[3] = estado[3] + 50
                    estado[0] = estado[0] - 1
                    urro = True

        if agente[2] == '>':
            # verifico se o Wumpus esta na sala para a qual o agente disparou a flecha
            for i in range(agente[1], len(mundo[0])):
                if mundo[agente[0]][i] == 2:
                    estado[3] = estado[3] + 50
                    estado[0] = estado[0] - 1
                    urro = True

        if agente[2] == 'v':
            # verifico se o Wumpus esta na sala para a qual o agente disparou a flecha
            for i in range(agente[0], len(mundo)):
                if mundo[i][agente[1]] == 2:
                    estado[3] = estado[3] + 50
                    estado[0] = estado[0] - 1
                    urro = True

        if agente[2] == '<':
            # verifico se o Wumpus esta na sala para a qual o agente disparou a flecha
            for i in range(agente[1], 0, -1):
                if mundo[agente[0]][i] == 2:
                    estado[3] = estado[3] + 50
                    estado[0] = estado[0] - 1
                    urro = True

    if acao == 'G':
        # Registro a perda de -1 ponto
        estado[3] = estado[3] - 1
        if mundo[agente[0]][agente[1]] == 3:
            estado[2] = estado[2] - 1

    if acao == 'S':
        estado[3] = estado[3] - 1
        # Verifico se o agente esta na saida e esta carregando o ouro
        if (agente[0] == len(mundo) - 1 and agente[1] == 0) and estado[2] == 0:
            # registro de +100 pontos
            estado[3] = estado[3] + 100

    # -----------------------------------------------------------------------------------------------------------------------

    # primeiro verifico se as casas adjacentes ao agente estao dentro da matriz mundo e
    # faco a atualizacao de 'percebe' de acordo com seus conteudos

    # defino uma lista auxiliar para contabilizar os conteudos das casas adjacentes
    aux = []

    # verifico se a casa superior ao agente esta dentro do mundo
    if agente[0] - 1 >= 0:
        if mundo[agente[0] - 1][agente[1]] == 0:
            # acrescento o numero 0 na lista auxiliar apenas se ele nao foi adicionado anteriormente
            if 0 not in aux:
                aux.append(0)

        if mundo[agente[0] - 1][agente[1]] == 1:
            # acrescento o numero 10 na lista auxiliar apenas se ele nao foi adicionado anteriormente
            if 10 not in aux:
                aux.append(10)

        if mundo[agente[0] - 1][agente[1]] == 2:
            # acrescento o numero 100 na lista auxiliar apenas se ele nao foi adicionado anteriormente
            if 100 not in aux:
                aux.append(100)

    # Note que os elementos sao adicionados na lista auxiliar apenas uma vez. Por exemplo, mesmo que existam dois pocos adjacentes ao agente,
    # o numero 010 (que corresponde a uma brisa) devera ser contabilizado uma unica vez na percepcao do personagem.

    # verifico se a casa inferior ao agente esta dentro do mundo
    if agente[0] + 1 < len(mundo):
        # Para as condicoes seguintes valem as mesmas consideracoes feitas anteriormente.
        if mundo[agente[0] + 1][agente[1]] == 0:
            if 0 not in aux:
                aux.append(0)

        if mundo[agente[0] + 1][agente[1]] == 1:
            if 10 not in aux:
                aux.append(10)

        if mundo[agente[0] + 1][agente[1]] == 2:
            if 100 not in aux:
                aux.append(100)

    # verifico se a casa a direita do agente esta dentro do mundo
    if agente[1] + 1 < len(mundo[0]):
        # Mesmas consideracoes.
        if mundo[agente[0]][agente[1] + 1] == 0:
            if 0 not in aux:
                aux.append(0)

        if mundo[agente[0]][agente[1] + 1] == 1:
            if 10 not in aux:
                aux.append(10)

        if mundo[agente[0]][agente[1] + 1] == 2:
            if 100 not in aux:
                aux.append(100)

    # verifico se a casa a esquerda do agente esta dentro do mundo
    if agente[1] - 1 >= 0:
        # Mesmas consideracoes.;
        if mundo[agente[0]][agente[1] - 1] == 0:
            if 0 not in aux:
                aux.append(0)

        if mundo[agente[0]][agente[1] - 1] == 1:
            if 10 not in aux:
                aux.append(10)

        if mundo[agente[0]][agente[1] - 1] == 2:
            if 100 not in aux:
                aux.append(100)

    # O ouro so eh percebido pelo personagem se ambos estiverem na mesma casa. Portanto, para a percepcao do reflexo nao eh necessario
    # analisar as casas adjacentes, basta analisar a casa em que o personagem esta.

    if mundo[agente[0]][agente[1]] == 3 and estado[2] == 1:
        # Acrescento o numero 1 n lista auxiliar. O numero 1 so sera inserido uma vez, no momento em que o personagem estiver
        # na mesma sala que ele. Portanto, nao eh necessario verificar se esse numero ja foi adicionado anteriormente
        aux.append(1)

    soma = 0
    for i in aux:
        soma = soma + i
    # o elemento soma representa, portanto, o inteiro que ira representar a percepcao do agente em sua respectiva casa.
    # Assim, faco a atualizacao da matriz percebe:
    percebe[agente[0]][agente[1]] = soma

    # --------------------------------------------------------------------------------------------------------------

    # Agora que todas as acoes foram contabilizadas e as respectivas listas/matrizes atualizadas, basta devolver
    # ao programa principal

    return urro, choque, agente, percebe


def imprime_mundo(mundo):
    for i in range(len(mundo)):
        for j in range(len(mundo[0])):
            if mundo[i][j] == 0:
                mundo[i][j] = ''

            if mundo[i][j] == 1:
                mundo[i][j] = 'P'

            if mundo[i][j] == 2:
                mundo[i][j] = 'W'

            if mundo[i][j] == 3:
                mundo[i][j] = 'O'

    print('-' * (7 * len(mundo) + len(mundo) + 1))
    for i in range(len(mundo)):
        for k in range(len(mundo[0])):
            if k != (len(mundo) - 1):
                print('|{:^7}'.format(mundo[i][k]), end='')
            else:
                print('|{:^7}|'.format(mundo[i][k]))
        print('-' * (7 * len(mundo) + len(mundo) + 1))


def main(mundo, agente, estado, percebe, acao, choque, urro):
    while estado[3] > -2000 and acao != 'S':
        imprime_percepcao(percebe, agente, choque, urro)
        choque = False
        urro = False
        acao = str(input('Digite a acao desejada (M/T/D/E/G/S): '))
        urro, choque, agente, percebe = atualiza_percepcaoEagente(mundo, agente, estado, percebe, acao, choque, urro)

    # -------------------------------------------------------------------------------------------------------------
    # Corpo principal do programa


nome = 'entrada.txt'
# Defino a matriz mundo como sendo, de fato, a matriz que representa o mundo do jogo, e matriz_usuario
# o mundo que aparece na tela para o jogador
mundo, mundo_usuario = le_mundo(nome)
agente = [len(mundo) - 1, 0, '^']
estado = [1, 1, 1, 0]

# Construo a matriz percepcao e verifico seus valores iniciais
percebe = []
for i in range(len(mundo)):
    percebe = percebe + [[-1] * len(mundo)]

# a primeira atualizacao da matriz percebe (que deve ocorrer logo na primeira rodada do jogo e por isso esta sendo feita
# separadamente antes do loop de repeticao) eh a mais simples, visto que soh eh necessario avaliar a sala superior e a sala a direita do
# agente.
aux = []

if mundo[agente[0] - 1][agente[1]] == 0:
    aux.append(0)
if mundo[agente[0] - 1][agente[1]] == 1:
    aux.append(10)
if mundo[agente[0] - 1][agente[1]] == 2:
    aux.append(100)

if mundo[agente[0]][agente[1] + 1] == 0:
    if 0 not in aux:
        aux.append(0)
if mundo[agente[0]][agente[1] + 1] == 1:
    if 10 not in aux:
        aux.append(10)
if mundo[agente[0]][agente[1] + 1] == 2:
    if 100 not in aux:
        aux.append(100)

# Poderia tambem ocorrer uma situacao em que o ouro ja esta na primeira sala do jogo. Esse caso esta representado no 'if' abaixo
if mundo[agente[0]][agente[1]] == 3:
    aux.append(1)

soma = 0
for i in aux:
    soma = soma + i

percebe[agente[0]][agente[1]] = soma
# Note que essa atualizacao da matriz percebe, mesmo antes do inicio do jogo, foi feita da mesma maneira como na funca atualiza_percebeEagente

# defino uma variavel indicadora de passagem para apresentar o urro na tela (caso o Wumpus seja morto)
urro = False

# defino uma variavel indicadora de passagem para representar o choque (caso ocorra)
choque = False

imprime_percepcao(percebe, agente, choque, urro)
acao = str(input('Digite a acao desejada (M/T/D/E/G/S): '))
urro, choque, agente, percebe = atualiza_percepcaoEagente(mundo, agente, estado, percebe, acao, choque, urro)
main(mundo, agente, estado, percebe, acao, choque, urro)
print('Fim de jogo!')
print('Confira o mapa completo do mundo:')
imprime_mundo(mundo)
print('Pontuacao final: {}'.format(estado[3]))