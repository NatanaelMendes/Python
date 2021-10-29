entrada = int(input())

lista = input()
lista = lista.split(' ')

gabarito = []

for i in range(1, entrada):
    if int(lista[i - 1]) > int(lista[i]):
        gabarito += [1]
    elif int(lista[i - 1]) < int(lista[i]):
        gabarito += [0]
    else:
        gabarito += [2]

if int(lista[i - 1]) < int(lista[i]):
    gabarito += [1]
elif int(lista[i - 1]) > int(lista[i]):
    gabarito += [0]
else:
    gabarito += [2]

cont = 1
for i in range(entrada - 1):
    if gabarito[i] == gabarito[i + 1] or gabarito[i] == 2 or gabarito[i + 1] == 2:
        cont = 2
        break

if cont == 1:
    print(1)
else:
    print(0)