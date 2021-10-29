a = int(input())
cont = 0
i = 1
fibo = 1
natti = 1
aux = 0
while cont != a:
    if fibo == i:
        aux = fibo
        fibo = fibo + natti
        natti = aux
    else:
        cont += 1
        gabarito = i
    i +=1
print(gabarito)