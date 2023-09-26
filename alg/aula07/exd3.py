k = int(input("Entre com um número inteiro maior que 1: "))
primo = True
n = 0

for i in range(1, k+1):
    if (k % i) == 0:
        n = k + 1

if n > 2:
    primo = False

if primo:
    print(f"O número {k} é primo! ")
else:
    print(f"O número {k} não é primo. ")
