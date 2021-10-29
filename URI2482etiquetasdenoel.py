numero_traducoes = int(input())
traducoes = {}
for i in range(numero_traducoes):
    idioma = input()
    feliz = input()
    traducoes[idioma] = feliz
quantidade_de_crianca = int(input())
for i in range(quantidade_de_crianca):
    kid = input()
    fala = input()
    print(kid)
    print(f'{traducoes[fala]}')
    print()
