a = int(input())
print(a)
cem = 0
cinquenta = 0
vinte = 0
dez = 0
cinco = 0
dois = 0
um = 0
while a >= 100:
    cem += 1
    a = a - 100
while a >= 50:
    cinquenta += 1
    a = a - 50
while a >= 20:
    vinte += 1
    a = a - 20
while a >= 10:
    dez += 1
    a = a - 10
while a >= 5:
    cinco += 1
    a = a - 5
while a >= 2:
    dois += 1
    a = a - 2
while a >= 1:
    um += 1
    a = a - 1
print(f'{cem} nota(s) de R$ 100,00')
print(f'{cinquenta} nota(s) de R$ 50,00')
print(f'{vinte} nota(s) de R$ 20,00')
print(f'{dez} nota(s) de R$ 10,00')
print(f'{cinco} nota(s) de R$ 5,00')
print(f'{dois} nota(s) de R$ 2,00')
print(f'{um} nota(s) de R$ 1,00')