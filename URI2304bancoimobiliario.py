jogo = list(map(int, input().split()))
saldo = [jogo[0], jogo[0], jogo[0]]
for i in range(jogo[1]):
    jogadas = list(map(str, input().split()))
    if jogadas[0] == 'A':
        if jogadas[1] == "D":
            if jogadas[2] == "E":
                saldo[0] = saldo[0]+int(jogadas[3])
                saldo[1] = saldo[1]-int(jogadas[3])
            elif jogadas[2] == "F":
                saldo[0] = saldo[0] + int(jogadas[3])
                saldo[2] = saldo[2] - int(jogadas[3])
        elif jogadas[1] == "E":
            if jogadas[2] == "D":
                saldo[1] = saldo[1] + int(jogadas[3])
                saldo[0] = saldo[0] - int(jogadas[3])
            elif jogadas[2] == "F":
                saldo[1] = saldo[1] + int(jogadas[3])
                saldo[2] = saldo[2] - int(jogadas[3])
        elif jogadas[1] == "F":
            if jogadas[2] == "D":
                saldo[2] = saldo[2] + int(jogadas[3])
                saldo[0] = saldo[0] - int(jogadas[3])
            elif jogadas[2] == "E":
                saldo[2] = saldo[2] + int(jogadas[3])
                saldo[1] = saldo[1] - int(jogadas[3])
    elif jogadas[0] == 'V':
        if jogadas[1] == 'D':
            saldo[0] = saldo[0] + int(jogadas[2])
        elif jogadas[1] == 'E':
            saldo[1] = saldo[1] + int(jogadas[2])
        if jogadas[1] == 'F':
            saldo[2] = saldo[2] + int(jogadas[2])
    elif jogadas[0] == 'C':
        if jogadas[1] == 'D':
            saldo[0] = saldo[0] - int(jogadas[2])
        elif jogadas[1] == 'E':
            saldo[1] = saldo[1] - int(jogadas[2])
        if jogadas[1] == 'F':
            saldo[2] = saldo[2] - int(jogadas[2])
print(saldo[0], saldo[1], saldo[2])