entrada = int(input())
cont = 0
while entrada != 0:
    cont += 1
    sorteio = list(map(int, input().split()))
    for i in range(len(sorteio)):
        ganhador = sorteio[i]
        if (ganhador - 1) == sorteio.index(ganhador):
            print(f'Teste {cont}')
            print(ganhador)
            print()
    entrada = int(input())
