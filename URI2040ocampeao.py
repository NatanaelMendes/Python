n_times = int(input())
while n_times != 0:
    dic_equipe = {}
    for i in range(n_times):
        pontuacao = input().split()
        dic_equipe[pontuacao[0]] = int(pontuacao[1])
    for i in range(n_times // 2):
        jogos = input().split()
        aux = [int(i) * 3 for i in jogos[1].split('-')]
        if aux[0] > aux[1]:
            a = 5
            b = 0
        elif aux[0] < aux[1]:
            a = 0
            b = 5
        else:
            a = b = 1
        dic_equipe[jogos[0]] += aux[0] + a
        dic_equipe[jogos[2]] += aux[1] + b
    ganhador = [max(dic_equipe, key=dic_equipe.get), max(dic_equipe.values())]
    if ganhador[0] == 'Sport':
        print('O Sport foi o campeao com %d pontos :D' % ganhador[1])
    else:
        print(f'O Sport nao foi o campeao. O time campeao foi o {ganhador[0]} com {ganhador[1]} pontos :(')
    print()
    n_times = int(input())