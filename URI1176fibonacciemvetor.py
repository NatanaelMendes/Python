entrada = int(input())
for i in range(entrada):
    fib = int(input())
    if fib == 0:
        print('Fib(0) = 0')
    elif fib == 1:
        print('Fib(1) = 1')
    else:
        aux = 0
        b = 0
        c = 1
        for j in range(fib-1):
            aux = b + c
            b = c
            c = aux
        print(f'Fib({fib}) = {aux}')
