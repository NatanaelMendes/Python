i = 0
a, b, c, d = map(int, input().split())
while i >= 10 ** 9:
    if (i % a == 0) and (i % b != 0) and (c % i == 0) and (d % i != 0):
        print(i)
    else:
        i += 1
