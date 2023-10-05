frase = input("Digite uma frase: ")

a = frase.lower().count('a')
e = frase.lower().count('e')
i = frase.lower().count('i')
o = frase.lower().count('o')
u = frase.lower().count('u')

print(f"A frase possui {a + e + i + o + u} vogais.")

frase = input("Digite uma frase: ")
qtd = 0
for letra in frase:
    if letra.lower() in 'aeiou':
        qtd += 1

print(f"A frase possui {qtd} vogais.")