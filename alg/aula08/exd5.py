frase = input("Digite uma frase: ")
palavra = input("Digite uma palavra: ")
qntPalavraUser = frase.lower().count(palavra)
qntPalavras = frase.split(' ')

print(f"A frase possui {len(qntPalavras)} palavras e repete {qntPalavraUser} a palavra {palavra}." )
