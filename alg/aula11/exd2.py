primos = []
i = 0
inicio = 100

while i < 10:
    primo = True
    for k in range(2, inicio//2):
        if (inicio % k) == 0:
            primo = False
            break
    if primo:
        primos.append(inicio)
        i = i + 1

    inicio = inicio + 1

t = tuple(primos)

for x in range(len(t)):
    print(t[x], end='-')
