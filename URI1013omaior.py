ent = list(map(int, input().split()))
aux = ent[0]
for i in range(len(ent)):
    if aux < ent[i]:
        aux = ent[i]
print('%.d eh o maior' %aux)