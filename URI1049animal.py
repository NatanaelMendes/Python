coluna = input()
filo = input()
alimentacao = input()
if coluna == 'vertebrado':
    if filo == 'ave':
        if alimentacao == 'carnivoro':
            print('aguia')
        else:
            print('pombo')
    else:
        if alimentacao == 'onivoro':
            print('homem')
        else:
            print('vaca')
else:
    if filo == 'inseto':
        if alimentacao == 'hematofago':
            print('pulga')
        else:
            print('lagarta')
    else:
        if alimentacao == 'hematofago':
            print('sanguessuga')
        else:
            print('minhoca')
