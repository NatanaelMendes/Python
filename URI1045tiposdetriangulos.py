lista = list(map(float, input().split()))
lista.sort()
if lista[2] >= lista[0] + lista[1]:
    print('NAO FORMA TRIANGULO')
else:
    if lista[2]**2 == lista[0]**2 + lista[1]**2:
        print('TRIANGULO RETANGULO')
    if lista[2]**2 > lista[0]**2 + lista[1]**2:
        print('TRIANGULO OBTUSANGULO')
    if lista[2]**2 < lista[0]**2 + lista[1]**2:
        print('TRIANGULO ACUTANGULO')
    if lista[2] == lista[0] or lista[2] == lista[1] or lista[0] == lista[1]:
        if lista[2] == lista[0] == lista[1]:
            print('TRIANGULO EQUILATERO')
        else:
            print('TRIANGULO ISOSCELES')