n, m = map(int, input().split())
lista = list(map(int, input().split()))
aux = 'S'
gabarito = []
for i in range(len(lista)):
    if i > 0:
        gabarito.append(lista[i] - lista[i-1])
gabarito.append(42195 - lista[n-1])
for j in range(len(gabarito)):
    if gabarito[j] > m:
        aux = 'N'
        break
    else:
        aux = 'S'
print(aux)