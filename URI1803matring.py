linha1 = input()
linha2 = input()
linha3 = input()
linha4 = input()
fff = linha1[0] + linha2[0] + linha3[0] + linha4[0]
lll = linha1[-1] + linha2[-1] + linha3[-1] + linha4[-1]
gabarito = ''
for i in range(1, len(linha1) - 1):
    letra = linha1[i] + linha2[i] + linha3[i] + linha4[i]
    c = (int(fff) * int(letra) + int(lll)) % 257
    gabarito += chr(c)
print(gabarito)
