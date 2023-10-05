while True:
    valor = input("Digite os numeros: ")
    if valor.isdigit() and len(valor) == 9:
        break
    if len(valor) != 9:
        print("Tem que ter 9 digitos!: ")
    else:
        print("Digite apenas numeros!: ")

novoValor = valor[0] + "." + valor[1:4]  + "." + valor[4:7] + "." + valor[4:7] + "," + valor[7:9]

print(f"{novoValor}")