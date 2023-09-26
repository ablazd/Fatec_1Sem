while True:
    b = float(input("Entre com a base: "))
    if b > 0:
        break
    print("O valor digitado é inválido. ")
while True:
    a = float(input("Entre com a altura: "))
    if a > 0:
        break
    print("O valor digitado é inválido. ")

area = (b * a) / 2
print(f"A área do triângulo é {area:5.2f}")
