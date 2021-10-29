import math
pontoa = list(map(float, input().split()))
pontob = list(map(float, input().split()))
distanciax = (pontob[0] - pontoa[0]) ** 2
distanciay = (pontob[1] - pontoa[1]) ** 2
distancia = math.sqrt(distanciax+distanciay)
print(round(distancia, 4))