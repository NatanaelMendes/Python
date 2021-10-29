lista = [0] * 20
aux = [0] * 20
j = 19
for i in range(20):
    lista[i] = int(input())
    aux[j-i] = lista[i]
for i in range(20):
    print(f'N[{i}] = {aux[i]}')