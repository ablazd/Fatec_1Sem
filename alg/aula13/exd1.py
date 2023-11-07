def ehpar(num):
    if num % 2 == 0:
        return True
    else:
        return False


x = int(input("Digite um número: "))
if ehpar(x):
    print('O número é par! ')
else:
    print('O número é ímpar! ')

'''
num = int(input('Digite um número: '))
print(ehpar(num))
'''
