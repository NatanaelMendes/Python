def um_aluno():
    estudantes = input()
    chamada = input()
    contp = 0
    conta = 0
    for i in range(len(chamada)):
        if chamada[i] == 'A':
            conta +=1
        elif chamada[i] =='P':
            contp += 1
    if (contp/(conta+contp)) < 0.75:
        print(estudantes)
    else:
        print()


def mais_de_um():
    estudantes = list(map(str, input().split()))
    chamada = list(map(str, input().split()))
    lista_ausente = []
    for i in range(len(estudantes)):
        contp = 0
        conta = 0
        for j in range(len(chamada[i])):
            if chamada[i][j] == 'A':
                conta += 1
            elif chamada[i][j] == 'P':
                contp += 1
        if (contp/(conta + contp)) < 0.75:
            lista_ausente.append(estudantes[i])
    if len(lista_ausente) > 0:
        for k in range(len(lista_ausente)):
            if k < (len(lista_ausente)-1):
                print(f'{lista_ausente[k]}', end= ' ')
            else:
                print(f'{lista_ausente[k]}', end= '')
        print()
    else:
        print()


casos = int(input())
for i in range(casos):
    a = int(input())
    if a > 1:
        mais_de_um()
    else:
        um_aluno()