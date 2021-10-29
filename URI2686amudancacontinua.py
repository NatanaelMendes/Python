while True:
    try:
        m = float(input())
        horas = int(m // 15)
        minutos = int(((m % 15)*60) // 15)
        segundos = int(((((m % 15)*60) % 15)*60) / 15)
        if m >= 90 and m < 180:
            print('Boa Tarde!!')
            print(f'{horas+6:02}:{minutos:02}:{segundos:02}')
        elif m >= 180 and m < 270:
            print('Boa Noite!!')
            print(f'{horas+6:02}:{minutos:02}:{segundos:02}')
        elif m >= 270 and m < 360:
            print('De Madrugada!!')
            print(f'{horas-18:02}:{minutos:02}:{segundos:02}')
        elif m >= 0 and m < 90:
            print('Bom dia!!')
            print(f'{horas+6:02}:{minutos:02}:{segundos:02}')
    except EOFError:
        break