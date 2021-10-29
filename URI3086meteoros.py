lista = list(map(int, input().split()))
cont = 0
meteoro = 0
while lista[0] != 0 and lista[1] != 0 and lista[2] != 0 and lista[3] != 0:
    cont +=1
    n = int(input())
    for i in range(n):
        aux = list(map(int, input().split()))
        if lista[0] <= aux[0] <= lista[2] and lista[3] <= aux[1] <= lista[1]:
            meteoro +=1
    print(f'Teste {cont}')
    print(meteoro)
    lista = list(map(int, input().split()))
    meteoro = 0