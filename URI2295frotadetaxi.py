a, b, c, d = map(float, input().split())
alcool = (10000/c) * a
gasolina = (10000/d) * b
if gasolina >= alcool:
    print('G')
else:
    print('A')