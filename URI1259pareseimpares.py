a = int(input())
lista1 = []
lista2 = []
for i in range(a):
    aux = int(input())
    if aux % 2 == 0:
        lista2.append(aux)
    else:
        lista1.append(aux)
lista1.sort(reverse=True)
lista2.sort()
for i in range(len(lista2)):
    print(f'{lista2[i]}')
for i in range(len(lista1)):
    print(f'{lista1[i]}')