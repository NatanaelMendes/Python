from functools import cmp_to_key as poote


def coisa(a, b):
    if int(a[1]) > int(b[1]) or (int(a[1]) == int(b[1]) and int(a[2]) > int(b[2])) or (
            int(a[1]) == int(b[1]) and int(a[2]) == int(b[2]) and int(a[3]) > int(b[3])) or (
            int(a[1]) == int(b[1]) and int(a[2]) == int(b[2]) and int(a[3]) == int(b[3]) and a[0] < b[0]):
        return -1
    elif int(a[1]) < int(b[1]) or (int(a[1]) == int(b[1]) and int(a[2]) < int(b[2])) or (
            int(a[1]) == int(b[1]) and int(a[2]) == int(b[2]) and int(a[3]) < int(b[3])) or (
            int(a[1]) == int(b[1]) and int(a[2]) == int(b[2]) and int(a[3]) == int(b[3]) and a[0] > b[0]):
        return +1
    else:
        return 0


def uvopormo(ee, x):
    print(ee[x][0] + " " + str(ee[x][1]) + " " + str(ee[x][2]) + " " + str(ee[x][3]))


n = int(input())
lalo = []
for i in range(n):
    lalo.append(list(input().split(" ")))
lalo.sort(key=poote(coisa))
i = 0
for ele in lalo:
    uvopormo(lalo, i)
    i = i + 1