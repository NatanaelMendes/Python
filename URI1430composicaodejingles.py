notas = dict([('W', 64), ('H', 32), ('Q', 16), ('E', 8), ('S', 4), ('T', 2), ('X', 1)])
entrada = input()
while entrada != '*':
    compasso = list(map(str, entrada.split('/')))
    aux = 0
    for i in range(len(compasso)):
        cont = 0
        for j in range(len(compasso[i])):
            cont += notas[compasso[i][j]]
        if cont == 64:
            aux += 1
    print(aux)
    entrada = input()
