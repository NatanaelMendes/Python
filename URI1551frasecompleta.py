alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
casos = int(input())
gabarito = []
for i in range(casos):
    frase = input()
    gabarito = alfabeto[:]
    for j in range(len(frase)):
        if frase[j] in gabarito:
            gabarito.remove(frase[j])
        if len(gabarito) == 0:
            break
    if len(gabarito) == 0:
        print('frase completa')
    elif 0 < len(gabarito) <= 13:
        print('frase quase completa')
    else:
        print('frase mal elaborada')