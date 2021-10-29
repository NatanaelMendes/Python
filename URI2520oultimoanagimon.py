while True:
    try:
        lista = list(map(int, input().split()))
        matrix = []
        for j in range(lista[0]):
            matrix.append(input().split())
        ash = [(index, j.index("1")) for index, j in enumerate(matrix) if "1" in j]
        pkm = [(index, j.index("2")) for index, j in enumerate(matrix) if "2" in j]
        if pkm[0][0] > ash[0][0]:
            quadrax = pkm[0][0] - ash[0][0]
        else:
            quadrax = ash[0][0] - pkm[0][0]
        if pkm[0][1] > ash[0][1]:
            quadray = pkm[0][1] - ash[0][1]
        else:
            quadray = ash[0][1] - pkm[0][1]
        print(quadrax + quadray)
    except EOFError:
        break
