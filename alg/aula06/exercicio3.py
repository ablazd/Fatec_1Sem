import math
largura = float(input("Entre com a largura do aposento: "))
comprimento = float(input("Agora com o comprimento: "))
altura = 2.8
porta = 0.8 * 2.1
gasto = (comprimento * altura) + ((largura * altura) - porta)

tamanho_lata = (input("Sua lata é de (1), (3) ou (18) litros?"))
if tamanho_lata == "1":
    qtd_lata1 = (math.ceil(gasto / 3))
    print(f"Você irá precisar de {qtd_lata1} lata(s) de tinta!")
elif tamanho_lata == "3":
    qtd_lata1 = (math.ceil(gasto / 9))
    print(f"Você irá precisar de {qtd_lata1} lata(s) de tinta!")
elif tamanho_lata == "18":
    qtd_lata1 = (math.ceil(gasto / 54))
    print(f"Você irá precisar de {qtd_lata1} lata(s) de tinta!")
else:
    print("Você inseriu um valor invalido. ")
