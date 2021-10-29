a = float(input()) * 100
cem = 0
cinquenta = 0
vinte = 0
dez = 0
cinco = 0
dois = 0
um = 0
mcinquenta = 0
mvinteecinco = 0
mdez = 0
mcinco = 0
mum = 0
while a >= 10000:
    cem += 1
    a = a - 10000
while a >= 5000:
    cinquenta += 1
    a = a - 5000
while a >= 2000:
    vinte += 1
    a = a - 2000
while a >= 1000:
    dez += 1
    a = a - 1000
while a >= 500:
    cinco += 1
    a = a - 500
while a >= 200:
    dois += 1
    a = a - 200
while a >= 100:
    um += 1
    a = a - 100
while a >= 50:
    mcinquenta +=1
    a = a - 50
while a >= 25:
    mvinteecinco += 1
    a = a - 25
while a >= 10:
    mdez += 1
    a = a - 10
while a >= 5:
    mcinco += 1
    a = a - 5
while a >= 1:
    mum +=1
    a = a- 1
print('NOTAS:')
print(f'{cem} nota(s) de R$ 100.00')
print(f'{cinquenta} nota(s) de R$ 50.00')
print(f'{vinte} nota(s) de R$ 20.00')
print(f'{dez} nota(s) de R$ 10.00')
print(f'{cinco} nota(s) de R$ 5.00')
print(f'{dois} nota(s) de R$ 2.00')
print('MOEDAS:')
print(f'{um} moeda(s) de R$ 1.00')
print(f'{mcinquenta} moeda(s) de R$ 0.50')
print(f'{mvinteecinco} moeda(s) de R$ 0.25')
print(f'{mdez} moeda(s) de R$ 0.10')
print(f'{mcinco} moeda(s) de R$ 0.05')
print(f'{mum} moeda(s) de R$ 0.01')
