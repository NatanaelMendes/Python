gabarito = str(input())
texto = str(input())
for i in range(len(texto)):
    print(chr(gabarito.index(texto[i]) + 97), end='')
print()