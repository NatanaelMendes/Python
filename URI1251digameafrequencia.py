while True:
    try:
        texto = list(map(str, input()))
        texto.sort(reverse=True)
        matrix = []
        aux = []
        for i in range(len(texto)):
            a = aux.count(texto[i])
            if a == 0:
                aux.append(texto.count(texto[i]))
                aux.append(ord(texto[i]))
                matrix.append(aux)
        print(matrix)
    except EOFError:
        break