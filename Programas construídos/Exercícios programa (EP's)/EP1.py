#Nome: Lucas de Paula Oliveira
#Numero usp: 11222179
#Codigo de um programa que analise as notas e a frequencia de um aluno e informe sua situacao final na disciplina
tot = int(input('Digite a quantidade de alunos da turma: '))
cont = 1
aprovados = 0
reprovados = 0
while cont <= tot :
    print ()
    print ('***************************************************************')
    print ('Aluno ',cont)
    cont = cont+1
    freq = int(input('Informe a frequencia do aluno: '))
    p1 = int(input('Informe a nota da p1: '))
    p2 = int(input('Informe a nota da p2: '))
    p3 = int(input('Informe a nota da p3: '))
    p_sub = int(input('Informe a nota da prova substitutiva: '))
    ep1 = int(input('Informe a nota do primeiro EP: '))
    ep2 = int(input('Informe a nota do segundo EP: '))
    ep3 = int(input('Informe a nota do terceiro EP: '))
    if p1 == -1 or (p1 == -1 and p2 == -1) or (p1 == -1 and p3 == -1) :
        p1 = p_sub
    if p2 == -1 or (p2 == -1 and p3 == -1):
        p2 = p_sub
    if p3 == -1:
        p3 = p_sub
    if p1 == -1 and p_sub == -1:
        p1 = 0
    if p2 == -1 and p_sub == -1:
        p2 = 0
    if p3 == -1 and p_sub == -1:
        p3 = 0
    if ep1 == -1:
        ep1 = 0
    if ep2 == -1:
        ep2 = 0
    if ep3 == -1:
        ep3 = 0
    media_provas = (p1+p2+p3)//3
    media_ep = (ep1 + 2*ep2 + 2*ep3)//5
    print ()
    if freq >= 70:
        if media_ep >= 50 and media_provas >= 50:
            media_final = (2*media_provas + media_ep)//3
            print('Frequencia: ',freq)
            print('Media das provas: ',media_provas)
            print('Media dos EPs: ',media_ep)
            print('Media final: ',media_final)
            if media_final >= 50:
                print('Situacao: Aprovado')
                aprovados = aprovados+1
            if media_final >= 30 and media_final < 50:
                p_rec = int(input('Informe a nota da prova de recuperacao: '))
                media_final_rec = (media_final + 2*p_rec)//3
                print ('Media final apos recuperacao: ',media_final_rec)
                if media_final_rec >= 50:
                    print('Situacao: Aprovado')
                    aprovados = aprovados+1
                else:
                    print('Situacao: Reprovado por nota')
                    reprovados = reprovados+1
            if media_final < 30:
                print ('Situacao: Reprovado por nota')
                reprovados=reprovados+1
        if media_ep < 50 or media_provas < 50 :
            if media_ep < media_provas:
                media_final = media_ep
                print ('Frequencia: ',freq)
                print ('Media das provas: ',media_provas)
                print ('Media dos EPs: ',media_ep)
                if media_final >= 30 and media_final < 50:
                    p_rec = int(input('Informe a nota da recuperacao: '))
                    media_final_rec = (media_final + 2*p_rec)//3
                    print ('Media final apos recuperacao: ',media_final_rec)
                    if media_final_rec >= 50:
                        print ('Situacao: Aprovado')
                        aprovados = aprovados+1
                    else:
                        print('Situacao: Reprovado por nota')
                        reprovados = reprovados+1
                if media_final < 30:
                    print ('Situacao: Reprovado por nota')
                    reprovados = reprovados+1
            if media_provas < media_ep:
                media_final = media_provas
                print ('Frequencia: ',freq)
                print ('Media das provas: ',media_provas)
                print ('Media dos EPs: ',media_ep)
                print ('Media final: ',media_final)
                if media_final >= 30 and media_final < 50:
                    p_rec = int(input('Informe a nota da prova de recuperacao: '))
                    media_final_rec = (media_final + 2*p_rec)//3
                    print ('Media final apos recuperacao: ',media_final_rec)
                    if media_final_rec >= 50:
                        print ('Situacao: Aprovado')
                        aprovados = aprovados+1
                    else:
                        print('Situacao: Reprovado por nota')
                        reprovados = reprovados+1
                if media_final < 30:
                    print ('Situacao: Reprovado por nota')
                    reprovados = reprovados+1
    else:
#Aqui o mesmo codigo se repete, apenas com algumas alteracoes das mensagens apresentadas na tela
        if media_ep >= 50 and media_provas >= 50:
            media_final = (2*media_provas + media_ep)//3
            print('Frequencia: ',freq)
            print('Media das provas: ',media_provas)
            print('Media dos EPs: ',media_ep)
            print('Media final: ',media_final)
            if media_final >= 50:
                print('Situacao: Reprovado por falta')
            if media_final >= 30 and media_final < 50:
                p_rec = int(input('Informe a nota da prova de recuperacao: '))
                media_final_rec = (media_final + 2*p_rec)//3
                print ('Media final apos recuperacao: ',media_final_rec)
                if media_final_rec >= 50:
                    print('Situacao: Reprovado por falta')
                else:
                        print('Situacao: Reprovado por nota e por falta')
            if media_final < 30:
                print ('Situacao: Reprovado por nota e por falta')
        if media_ep < 50 or media_provas < 50 :
            if media_ep < media_provas:
                media_final = media_ep
                print ('Frequencia: ',freq)
                print ('Media das provas: ',media_provas)
                print ('Media dos EPs: ',media_ep)
                if media_final >= 30 and media_final < 50:
                    p_rec = int(input('Informe a nota da prova de recuperacao: '))
                    media_final_rec = (media_final + 2*p_rec)//3
                    print ('Media final apos recuperacao: ',media_final_rec)
                    if media_final_rec >= 50:
                        print ('Situacao: Reprovado por falta')
                    else:
                        print('Situacao: Reprovado por nota e por falta')
                if media_final < 30:
                    print ('Situacao: Reprovado por nota e por falta')
            if media_provas < media_ep:
                media_final = media_provas
                print ('Frequencia: ',freq)
                print ('Media das provas: ',media_provas)
                print ('Media dos EPs: ',media_ep)
                print ('Media final: ',media_final)
                if media_final >= 30 and media_final < 50:
                    p_rec = int(input('Informe a nota da prova de recuperacao: '))
                    media_final_rec = (media_final + 2*p_rec)//3
                    print ('Media final apos recuperacao: ',media_final_rec)
                    if media_final_rec >= 50:
                        print ('Situacao: Reprovado por falta')
                    else:
                        print('Situacao: Reprovado por nota e por falta')
                if media_final < 30:
                     print ('Situacao: Reprovado por nota e por falta')
print ()
print ('Total de aprovados: ',aprovados)
print ('Total de reprovados: ',reprovados)