n = int(input())
while n !=0:
    gabarito = [[0] * 10 for i in range(6)]
    for i in range(n):
        entrada = input().split()
        telaa = list(map(int, entrada[0:2]))
        telab = list(map(int, entrada[2:4]))
        telac = list(map(int, entrada[4:6]))
        telad = list(map(int, entrada[6:8]))
        telae = list(map(int, entrada[8:10]))
        letra = entrada[10:16]
        for j in range(6):
            if letra[j] == 'A':
                d1 = telaa[0]
                d2 = telaa[1]
                gabarito[j][d1] += 1
                gabarito[j][d2] += 1
            elif letra[j] == 'B':
                d1 = telab[0]
                d2 = telab[1]
                gabarito[j][d1] += 1
                gabarito[j][d2] += 1
            elif letra[j] == 'C':
                d1 = telac[0]
                d2 = telac[1]
                gabarito[j][d1] += 1
                gabarito[j][d2] += 1
            elif letra[j] == 'D':
                d1 = telad[0]
                d2 = telad[1]
                gabarito[j][d1] += 1
                gabarito[j][d2] += 1
            elif letra[j] == 'E':
                d1 = telae[0]
                d2 = telae[1]
                gabarito[j][d1] += 1
                gabarito[j][d2] += 1
    password = []
    for k in range(6):
        max = gabarito[0][k]
        posicao = 0
        for lm in range(10):
            if max < gabarito[k][lm]:
                posicao = lm
        password.append(posicao)
    print(password)
    n = int(input())