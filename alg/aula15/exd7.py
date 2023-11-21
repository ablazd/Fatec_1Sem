def reverso(num):
    numReverso = int(str(num)[::-1])
    return numReverso

numero = int(input('Digite um número: '))
print(f"O reverso do número {numero} é {reverso(numero)}")
