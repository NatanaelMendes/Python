entrada = int(input())
cont = 0
while entrada!=0:
    par = input()
    impar = input()
    cont += 1
    print('Teste', cont)
    for i in range(entrada):
        c = input()
        a, b = map(int, c.split())
        if (a + b) % 2 == 0:
            print(par)
        elif (a+b) % 2 != 0:
            print(impar)
    print()
    entrada = int(input())