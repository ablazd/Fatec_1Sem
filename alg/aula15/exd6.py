def quantDigito(num):
    digitos = int(len(str(num)))
    return digitos

print(f"O número possui {quantDigito(int(input('Digite um numero inteiro: ')))} digitos.")
