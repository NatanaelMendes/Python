    def andar(aux):
        if aux.count('SAME AS') > 0:
            return(int(aux[j][-1])


total = int(input())
for i in range(total):
    position = 0
    lista = []
    passos = int(input())
    for j in range(passos):
        lista.append(input())
    aux = 'SAME AS'
    for j in range(len(lista)):
        if lista[j].count(aux) > 0:
            volta = int(lista[j][-1])
            if lista[volta] == 'LEFT':
                position -= 1
            elif lista[volta] == 'RIGHT':
                position += 1
        else:
            if lista[j] == 'LEFT':
                position -= 1
            elif lista[j] == 'RIGHT':
                position += 1
    print(position)