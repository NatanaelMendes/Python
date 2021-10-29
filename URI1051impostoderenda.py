renda = (float(input()))
if renda <= 2000:
    print('Isento')
elif 2000.00 < renda <= 3000:
    a = (renda - 2000) * 0.08
    print('R$ %.2f' %a)
elif 3000.00 < renda <= 4500:
    b = ((renda - 3000) * 0.18) + 80
    print('R$ %.2f' %b)
elif renda > 4500:
    c = ((renda - 4500) * 0.28) + 350
    print('R$ %.2f' %c)