total = int(input())
for i in range(total):
    a, b = map(str, input().split())
    aux = a[len(a) - len(b):]
    cont = aux.count(b)
    if cont > 0:
        print('encaixa')
    else:
        print('nao encaixa')
