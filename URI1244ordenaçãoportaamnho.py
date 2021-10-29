entrada = int(input())
i = 0
while i < entrada:
    frase = list(map(str, input().split()))
    frase.sort(key=len, reverse=True)
    for j, k in enumerate(frase):
        print(f'{k}', end='')
        if j != len(frase)-1:
            print(' ', end='')
    print()
    i += 1
