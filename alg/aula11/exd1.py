lista = []
i = 0

while i < 10:
    x = int(input("Digite um número: "))
    lista.append(x)
    i = i + 1

t = tuple(lista)
print(t[::-1])
