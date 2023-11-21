import random

def embaralha(palavra):
    palavra = list(palavra)
    for i in range(len(palavra) - 1):
        posicaoAleatoria = random.randint(i + 1, len(palavra) - 1)
        palavra[i], palavra[posicaoAleatoria] = palavra[posicaoAleatoria], palavra[i]
    palavra = "".join(palavra)
    return palavra.lower()

print(embaralha(input('Digite uma palavra: ')))
