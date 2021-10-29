ciclos = int(input())
entrada = list(map(int, input().split()))
i = 1
aux = entrada[0]
saida = 0
while i < ciclos:
    if aux <= entrada[i]:
        aux = entrada[i]
    elif aux > entrada[i]:
        saida = i+1
        break
    i += 1
print(saida)