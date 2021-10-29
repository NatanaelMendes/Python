entrada = input()
aux = 0
for i in range(len(entrada)):
    if entrada[i] == '1':
        aux += 1
if aux % 2 != 0:
    entrada += '1'
    print(entrada)
else:
    entrada += '0'
    print(entrada)
