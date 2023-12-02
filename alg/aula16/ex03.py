from math import prod

num = str(input("Digite o RA: "))
ls_num = list(num)
lista_inteiro = []

for i in ls_num:
    lista_inteiro += [int(i)]

print(f"Soma = {sum(lista_inteiro)}")
print(f"Multiplicação = {prod(lista_inteiro)}")
