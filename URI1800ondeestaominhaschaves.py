quantidade, visitados = map(int, input().split())
ultimos = list(map(int, input().split()))
for i in range(quantidade):
    a = int(input())
    if a in ultimos:
        print(0)
    else:
        print(1)
        ultimos.append(a)
