lista = []

for i in range(10):
    lista.append(int(input(f'Digite o número {i+1}: ')))

'''
lista.reverse()
print(lista)
'''

for i in lista[::-1]:
    print(i, end=' ')
print()
print(lista)
