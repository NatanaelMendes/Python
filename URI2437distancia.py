a, b, c, d = map(int, input().split())
soma = 0
if a < c:
    soma += c - a
elif a > c:
    soma += a - c
if b < d:
    soma += d - b
elif b > d:
    soma += b - d
print(soma)