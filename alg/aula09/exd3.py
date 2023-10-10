from random import randint

lista = [0] * 7

for _ in range(6000):
    n = randint(1, 6)
    lista[n] = lista[n]+1

p = [0] * 7

for i in range(1, 7):
    p[i] = (lista[i] / 6000) * 100
    print(f'{i} - {p[i]:.2f}% - {lista[i]}')
