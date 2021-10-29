a, b, c = map(float, input().split())
if a >= (b+c) or b >= (c+a) or c >= (a+b):
    area = ((a+b)*c)/2
    print('Area =', round(area, 1))
else:
    p = a+b+c
    print('Perimetro =', round(p, 1))
