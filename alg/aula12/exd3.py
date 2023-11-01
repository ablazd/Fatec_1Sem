lista1 = []
lista2 = []

for i in range(1, 6):
    lista1.append(int(input("Digite um número para lista 01: ")))
for i in range(1, 6):
    lista2.append(int(input("Digite um número para lista 02: ")))
set1 = set(lista1)
set2 = set(lista2)


print(set1.union(set2))
