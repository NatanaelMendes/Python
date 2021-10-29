def adiciona():
    a = []
    for i in range(coluna + 2):
        a.append(0)
    matrix.append(a)


linha, coluna = map(int, input().split())
matrix = []
adiciona()
for i in range(linha):
    vet = list(map(int, input().split()))
    vet.append(0)
    vet = [0] + vet
    matrix.append(vet)
adiciona()
x = y = 0
for i in range(1, linha + 1):
    for j in range(1, coluna + 1):
        if matrix[i][j] == 42:
            if (matrix[i - 1][j] == 7) and (matrix[i+1][j] == 7) and (matrix[i][j-1] == 7) and (matrix[i][j+1] == 7) and (matrix[i- 1][j- 1] == 7) and (matrix[i + 1][j + 1] == 7) and (matrix[i - 1][j + 1] == 7) and (matrix[i + 1][j - 1] == 7):
                x = i
                y = j
                break
if x == y == 0:
    print('0 0')
else:
    print(f'{x} {y}')
