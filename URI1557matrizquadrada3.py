entrada = int(input())

while entrada != 0:
    matrix = []
    linha = []
    for i in range(entrada):
        linha.append(2 ** i)
    matrix.append(linha)
    for i in range(entrada - 1):
        linha = []
        for j in range(entrada):
            linha.append(matrix[i][j] * 2)
        matrix.append(linha)

    a = str(matrix[entrada - 1][entrada - 1])
    espaco = len(a)
    for i in range(entrada):
        for j in range(entrada):
            matrix[i][j] = str(matrix[i][j])
            while len(matrix[i][j]) < espaco:
                matrix[i][j] = ' ' + matrix[i][j]
        matrixFinal = ' '.join(matrix[i])

        print(matrixFinal)
    print()

    entrada = int(input())
