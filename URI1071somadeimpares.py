a = int(input())
b = int(input())
if a > b:
    maior = a
    menor = b
else:
    maior = b
    menor = a
if menor % 2 != 0:
    menor += 1
soma = 0
while menor < maior:
    if menor % 2 != 0:
        soma = soma + menor
    menor +=1
print(soma)