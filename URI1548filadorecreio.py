testes = int(input())
for i in range(testes):
    aluno = int(input())
    fila = list(map(int, input().split()))
    gabarito = fila[:]
    gabarito.sort(reverse=True)
    cont = 0
    for j in range(aluno):
        if gabarito[j] == fila[j]:
            cont +=1
    print(cont)