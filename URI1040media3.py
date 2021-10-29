a, b, c, d = map(float, input().split())
media = ((a*2)+(b*3)+(c*4)+(d*1))/10
print('Media:', round(media, 1))
if media >= 7:
    print('Aluno aprovado.')
elif media < 5:
    print('Aluno reprovado.')
else:
    print('Aluno em exame.')
    e = float(input())
    print('Nota do exame:', round(e, 1))
    media = (media + e)/2
    if media >= 5:
        print('Aluno aprovado.')
    else:
        print('Aluno reprovado.')
    print('Media final:', round(media, 1))