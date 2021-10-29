entrada = list(map(int, input().split()))
if entrada[0] >= entrada[1] >= entrada[2] >= entrada[3] >= entrada[4] and entrada[0] > entrada[4]:
    print('D')
elif entrada[4] >= entrada[3] >= entrada[2] >= entrada[1] >= entrada[0] and entrada[4] > entrada[0]:
    print('C')
else:
    print('N')
