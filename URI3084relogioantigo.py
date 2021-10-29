while True:
    try:
        h, m = map(int, input().split())
        if h >= 0 and h < 30:
            horas = 0
        else:
            horas = h // 30
        if m >= 0 and m < 6:
            minutos = 0
        else:
            minutos = m // 6
        print(f'{horas:02}:{minutos:02}')
    except EOFError:
        break