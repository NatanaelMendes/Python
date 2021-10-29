ddd = {'27': 'Vitoria', '31': 'Belo Horizonte', '19': 'Campinas', '61': 'Brasilia', '71': 'Salvador', '11': 'Sao Paulo', '21': 'Rio de Janeiro', '32': 'Juiz de Fora'}
ddd_entrada = input()
print(ddd.get(ddd_entrada, 'DDD nao cadastrado'))