instancias = int(input())
for i in range(instancias):
    lista = []
    palavra_japones = []
    listinha = []
    tradução = []
    n_palavras, n_linhas = (map(int, input().split()))
    for j in range(n_palavras):
        jap = input()
        trad = input()
        palavra_japones.append(jap)
        tradução.append(trad)
    dicionario = dict(zip(palavra_japones, tradução))
    for j in range(n_linhas):
        p = input()
        v = p.split(' ')
        lista.append(v)
    for j in range(n_linhas):
        lista2 = []
        for k in range(len(lista[j])):
            if dicionario.get(lista[j][k]) == None:
                lista2.append(lista[j][k])
            else:
                lista2.append(dicionario.get(lista[j][k]))
        print(' '.join(lista2))
    print('')