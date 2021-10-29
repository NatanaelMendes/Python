casos = int(input())
i = 0
while i != casos:
    padrao = input()
    cafe = input()
    almoco = input()
    janta = almoco + cafe
    for j in range(len(janta)):
        if janta[j] in padrao:
            padrao = padrao.replace(janta[j], "")
        else:
            padrao = "CHEATER"
            break
    dieta = sorted(padrao)
    if padrao != "CHEATER":
        padrao = "".join(dieta)
    print(padrao)
    i += 1