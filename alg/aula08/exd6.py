palavra = input("Digite uma palavra: ")
inverso = palavra[::-1]

if palavra.lower() == inverso.lower():
    print(f"A palavra {palavra} é palindroma.")
else:
    print(f"A palavra {palavra} não é palindroma.")
