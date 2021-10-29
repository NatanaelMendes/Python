entrada = list(map(int, input().split()))
horaa = entrada[0]
horab = entrada[2]
minutoa = entrada[1]
minutob = entrada[3]
if horab == 0:
    horab = 24
if horaa == 0:
    horaa = 24
hora = horab - horaa
minuto = minutob -minutoa
if minutob < minutoa:
    minuto = 60 + (minutob - minutoa)
    hora = hora - 1
if hora == minuto == 0:
    hora = 24
    minuto = 0
if hora < 0:
    hora = hora + 24
print(f'O JOGO DUROU {hora} HORA(S) E {minuto} MINUTO(S)')