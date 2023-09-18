a = float(input("Entre com o valor de a: "))
b = float(input("Entre com o valor de b: "))
c = float(input("Entre com o valor de c: "))

if (a+c > b) and (a+b > c) and (b+c > a):
    # é um triângulo
    if (a == b == c):
        print("É um triângulo equilátero.")
    elif (a == b) or (b == c) or (c == a):
        print("É um triângulo isósceles. ")
    else:
        print("É um triângulo escaleno.")
else:
    # não é um triângulo
    print("Não é um triângulo. ")


