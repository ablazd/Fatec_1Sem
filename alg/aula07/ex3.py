soma = 0
qtd = int(input(f"Entre com a quantidade de idades: "))
for i in range(1, qtd+1):
    n = int(input(f"Entre com a {i}a. idade: "))
    soma = soma + n
media = soma / qtd
print(f"A média das idades é {media:5.2f}")
