entrada = int(input())
cont = 0
while entrada != 0:
    lista = []
    maior = 0
    for i in range(entrada):
        lista.append(input())
        if maior < len(lista[i]):
            maior = len(lista[i])
    if cont > 0:
        print('')
    for item in lista:
        if len(item) < maior:
            aux = (' ' * (maior - (len(item))) + item)
            print(aux)
        else:
            print(item)
    cont +=1
    entrada = int(input())
