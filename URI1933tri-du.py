entrada = list(map(int, input().split()))
if entrada[0] == entrada[1]:
    print(entrada[0])
elif entrada[0] > entrada[1]:
    print(entrada[0])
elif entrada[0] < entrada[1]:
    print(entrada[1])