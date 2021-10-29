mac = {'1001': '1.5', '1002': '2.5', '1003': '3.5', '1004': '4.5', '1005': '5.5'}
fila = int(input())
total = 0
for i in range(fila):
    a, b = input().split()
    aux = (mac[a])
    total += float(aux) * float(b)
print(f'{total:.2f}')