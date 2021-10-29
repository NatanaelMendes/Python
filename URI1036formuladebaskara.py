import math
ent = list(map(float, input().split()))
delta = round((ent[1]**2) + (ent[0]*ent[2]*-4), 5)
if delta < 0 or ent[0] == 0:
    print('Impossivel calcular')
elif delta == 0:
    r1 = (ent[1]*-1)/(ent[0]*2)
    print('R1 = ', round(r1, 5))
    print('R2 =', round(r1, 5))
elif delta > 0:
    r1 = (ent[1]*(-1)+math.sqrt(delta))/(ent[0]*2)
    r2 = ((ent[1]*-1)-math.sqrt(delta))/(ent[0]*2)
    print('R1 =', round( r1, 5))
    print('R2 =', round( r2, 5))
