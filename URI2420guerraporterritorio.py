numero = int(input())
entrada = list(map(int, input().split()))
total = sum(entrada)/2
cont = 0
i = 0
while total != 0:
    cont +=1
    total = total - entrada[i]
    i+=1
print(cont)