casos = int(input())
feira = {}
for i in range(casos):
    total = 0
    frutas = int(input())
    for j in range(frutas):
        tem_na_feira = list(map(str, input().split()))
        feira[tem_na_feira[0]] = tem_na_feira[1]
    quantidade = int(input())
    for j in range(quantidade):
        chave , quant = map(str, input().split())
        quant = int(quant)
        total += float(feira[chave]) * quant
    print(f'R$ {total:.2f}')