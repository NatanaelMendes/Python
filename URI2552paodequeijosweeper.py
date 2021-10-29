def adiciona():
    a = []
    for i in range(coluna + 2):
        a.append(0)
    matrix.append(a)


while True:
    try:
        linha, coluna = map(int, input().split())
        matrix = []
        adiciona()
        for i in range(linha):
            vet = list(map(int, input().split()))
            vet.append(0)
            vet = [0] + vet
            matrix.append(vet)
        adiciona()
        for i in range(linha+1):
            for j in range(coluna+1):
                if matrix[i][j] == 1:
                    matrix[i][j] += 8
        for i in range(linha+1):
            for j in range(coluna+1):
                opa = 0
                if matrix[i][j] == 0:
                    if matrix[i - 1][j] == 9:
                        opa += 1
                    if matrix[i+1][j] == 9:
                        opa += 1
                    if matrix[i][j-1] == 9:
                        opa += 1
                    if matrix[i][j+1] == 9:
                        opa += 1
                    matrix[i][j] = opa
        for i in range(1, linha+1):
            for j in range(1, coluna+1):
                print(f'{matrix[i][j]}', end='')
            print()
    except EOFError:
        break