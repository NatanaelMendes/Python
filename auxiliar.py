dicio = []
for i in range(5):
    dicio.append(0)
dicio.append(2)
dicio = [1] + dicio
print(dicio)






























'''while True:
    try:
        lista = input().split()
        qtdLinhas, qtd_coluna = int(lista[0]), int(lista[1])
        matriz = []

        for i in range(qtdLinhas):
            matriz.append(input().split())

        minhaPosicao = [(index, j.index("1")) for index, j in enumerate(matriz) if "1" in j]
        analogimonPos = [(index, j.index("2")) for index, j in enumerate(matriz) if "2" in j]

        eixoX = (abs(analogimonPos[0][0]-minhaPosicao[0][0]))
        eixoY = (abs(analogimonPos[0][1] - minhaPosicao[0][1]))

        print(eixoX + eixoY)

    except EOFError:
        break'''



'''def um_aluno():
    estudantes = input()
    chamada = input()
    contp = 0
    conta = 0
    for i in range(len(chamada)):
        if chamada[i] == 'A':
            conta +=1
        elif chamada[i] =='P':
            contp += 1
    try:
        if (contp / (conta + contp)) <= 0.75:
            print(estudantes)
    except ZeroDivisionError:
        print(estudantes)


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
        um_aluno()'''





'''matrix = [[1, 0, 0], [0, 0, 2], [1]]
a = matrix[0].index(1)
print(a)'''

'''for i in range(m):
    for j in range(n):
        teste = matrix[i][j]
        if teste == 1:
            a = i
            b = j
        elif teste == 2:
            c = i
            d = j'''

'''def fun_eco(maior, menor):
    aux = maior - menor
    return(aux)


a, b, c, d = map(float, input().split())
if a >= b:
    gasolina = (fun_eco(a, b)) * d + d
    alcool = a * c
else:
    alcool = (fun_eco(b, a)) * c + c
    gasolina = b * d
if gasolina >= alcool:
    print('G')
else:
    print('A')'''






''''entrada = int(input())
matrix = []
linha = []
for j in range(entrada):
    linha.append(2 ** j)
matrix.append(linha)
for i in range(entrada - 1):
    linha = []
    for j in range(entrada):
        linha.append(matrix[i][j] * 2)
    matrix.append(linha)
print(matrix)'''





















''''matrix = []
for i in range(5):
    linha = []
    for j in range(5):
        linha.append(2**j)
    matrix.append(linha)
for i in range(5):
    print(matrix[i])'''

'''while True:
    try:
        texto = list(map(str, input()))
        texto.sort(reverse=True)
        gabarito = []
        matrix = []
        for i in range(len(texto)):
            a = texto.count(texto[i])
            if texto[i] in not gabarito:
                gabarito



    except EOFError:
        break'''