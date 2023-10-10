lista = []

for i in range(5):
    lista.append(int(input(f'Digite o número {i+1}: ')))

maior = sorted(lista, reverse=True)[0]
pos = lista.index(maior)

'''
pos = 0
maior = lista[pos]

for i in range(0, len(lista)):
    if lista[i] >= maior:
        maior = lista[i]
        pos = i
'''

print(f'O maior número da lista é {maior} no indice {pos}. ')

