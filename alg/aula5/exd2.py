nota1 = float(input("Entre com a primeira nota: "))
nota2 = float(input("Entre com a segunda nota: "))
nota3 = float(input("Entre com a terceira nota: "))
media = (nota1 + nota2 + nota3) / 3

if media < 3.0:
    resultado = "Reprovado"
else:
    if media < 7.0:
        resultado = "Exame"
        nota_exame = 12 - media
    else:
        resultado = "Aprovado"

print(f"Média {media:5.2f} - {resultado}! ")
if nota_exame != 0:
    print(f"Tem que tirar no minimo {nota_exame:5.2f} no exame de recuperação. ")

if media < 3.0:
    print(f"Média {media:5.2f} - Reprovado. ")
else:
    if media < 7.0:
        print(f"Média {media:5.2f} - Exame de recuperação. ")
    else:
        print(f"Média {media:5.2f} - Aprovado!")
