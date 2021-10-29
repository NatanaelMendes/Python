a, b = map(int, input().split())
matrix = []
for i in range(a):
    aux = list(map(int, input().split()))
    matrix.append(aux)
gabarito = []
for i in range(a):
    somal = 0
    for j in range(b):
        somal += matrix[i][j]
    gabarito.append(somal)
for i in range(b):
    somac = 0
    for j in range(a):
        somac += matrix[j][i]
    gabarito.append(somac)
maior = max(gabarito)
print(maior)