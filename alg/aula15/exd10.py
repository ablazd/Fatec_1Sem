quadrado = []
magico = False

for i in range(0, 9):
    quadrado.append(0)

def quadradoMagico():
    global magico
    if (
        quadrado[0] + quadrado[1] + quadrado[2] ==
        quadrado[0] + quadrado[3] + quadrado[6] ==
        quadrado[0] + quadrado[4] + quadrado[8] ==
        quadrado[3] + quadrado[4] + quadrado[5] ==
        quadrado[6] + quadrado[7] + quadrado[8] ==
        quadrado[6] + quadrado[4] + quadrado[2] ==
        quadrado[2] + quadrado[5] + quadrado[8]
    ):
        magico = True
    else:
        magico = False
    return magico

def gerarQuadrados(posicao):
    global magico
    if posicao == 9:
        quadradoMagico()
        if magico:
            print(f"\n\t{quadrado[0]} \t{quadrado[1]} \t{quadrado[2]} \n"
                  f"\t{quadrado[3]} \t{quadrado[4]} \t{quadrado[5]} \n"
                  f"\t{quadrado[6]} \t{quadrado[7]} \t{quadrado[8]} \n")
    else:
        numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for numero in numeros:
            if numero not in quadrado:
                quadrado[posicao] = numero
                gerarQuadrados(posicao + 1)
                quadrado[posicao] = 0

gerarQuadrados(0)
