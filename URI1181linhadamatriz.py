numero = int(input())
letra = input()
matrix = []
for i in range(12):
    linha = []
    for j in range(12):
        linha.append(float(input()))
    matrix.append(linha)
soma = 0
for i in range(12):
    soma += matrix[numero][i]
if letra == 'S':
    print(round(soma,1))
else:
    print(round(soma/12, 1))
