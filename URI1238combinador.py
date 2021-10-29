def combinar(pmaior, pmenor, inter):
    gabarito = ''
    for j in range(inter):
        if j < len(pmaior):
            gabarito += pmaior[j]
        if j < len(pmenor):
            gabarito += pmenor[j]
    print(gabarito)


casos = int(input())
for i in range(casos):
    palavra1, palavra2 = map(str, input().split())
    a = len(palavra1)
    b = len(palavra2)
    if a > b:
        maior = a
    else:
        maior = b
    combinar(palavra1, palavra2, maior)
