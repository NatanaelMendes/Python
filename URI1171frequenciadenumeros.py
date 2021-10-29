a = int(input())
entrada = []
for i in range(a):
    entrada.append(int(input()))
entrada.sort()
lista = []
gabarito = []
for i in range(a):
    if entrada[i] in gabarito:
        j = 0
    else:
        aux = entrada.count(entrada[i])
        lista.append(aux)
        gabarito.append(entrada[i])
for i in range(len(lista)):
    print(f'{gabarito[i]} aparece {lista[i]} vez(es)')

