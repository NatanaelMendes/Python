a, b, c, d = map(int, input().split())
if b > d:
    divisor = b
else:
    divisor = d
while (divisor % b != 0) or (divisor % d != 0):
    divisor +=1
dividendo = int((a * (divisor/b)) + (c * (divisor/d)))
mdc = 1
if dividendo > divisor:
    maior = dividendo
else:
    maior = divisor
while True:
    if dividendo % maior == 0 and divisor % maior == 0:
        mdc = maior
        break
    maior -= 1
print(f'{dividendo/mdc:.0f} {divisor/mdc:.0f}')
