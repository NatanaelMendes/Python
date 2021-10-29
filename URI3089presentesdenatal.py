n = int(input())
while n != 0:
    valor = list(map(int, input().split()))
    valor.sort()
    gabarito = []
    i, j = 0, len(valor)
    while True:
        maior = valor[i]
        menor = valor[j-1]
        soma = maior + menor
        gabarito.append(soma)
        i += 1
        j -= 1
        if j < i:
            break
    print(max(gabarito), min(gabarito))
    n = int(input())
