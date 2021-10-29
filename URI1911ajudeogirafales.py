n_assinatura = int(input())
while n_assinatura != 0:
    gabarito = {}
    for i in range(n_assinatura):
        chave = input()
        assinatura = input()
        gabarito[chave] = assinatura
    n_alunos = int(input())
    cont = 0
    for i in range(n_alunos):
        nome = input()
        assin = input()
        confere = 0
        aux = gabarito[nome]
        for j in range(len(assin)):
            if aux[j] != assin[j]:
                confere += 1
        if confere > 1:
            cont += 1
    print(cont)
    n_assinatura = int(input())