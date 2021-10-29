entrada = input()
matrix = []
if entrada == 'S' or entrada == 'M':
    for i in range(12):
        linha = []
        for j in range(12):
            linha.append(float(input()))
        matrix.append(linha)
    soma = 0
    for i in range(7, 12):
        if i == 7:
            soma += matrix[i][5] + matrix[i][6]
        elif i == 8:
            soma += matrix[i][4] + matrix[i][5] +matrix[i][6] + matrix[i][7]
        elif i == 9:
            soma += matrix[i][3] + matrix[i][4] + matrix[i][5] + matrix[i][6] + matrix[i][7] + matrix[i][8]
        elif i == 10:
            soma += matrix[i][2] + matrix[i][3] + matrix[i][4] + matrix[i][5] + matrix[i][6] + matrix[i][7] + matrix[i][8] + matrix[i][9]
        elif i == 11:
            soma += matrix[i][1] + matrix[i][2] + matrix[i][3] + matrix[i][4] + matrix[i][5] + matrix[i][6] + matrix[i][7] + matrix[i][
                8] + matrix[i][9] + matrix[i][10]
    if entrada == 'S':
        print(round(soma, 1))
    else:
        print(round(soma/30, 1))