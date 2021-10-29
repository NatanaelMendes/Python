partidas = int(input())
while partidas != 0:
    a = 0
    b = 0
    for i in range(partidas):
        entrada = list(map(int, input().split()))
        if entrada[0] > entrada[1]:
            a +=1
        elif entrada[0] < entrada[1]:
            b +=1
    print(a, b)
    partidas = int(input())