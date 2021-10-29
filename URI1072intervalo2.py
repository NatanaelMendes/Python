numero = int(input())
contin = 0
contout = 0
for i in range(numero):
    aux = int(input())
    if 10 <= aux <= 20:
        contin += 1
    else:
        contout += 1
print(f'{contin} in')
print(f'{contout} out')