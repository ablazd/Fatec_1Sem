nome = input("Digite seu nome: ")
idade = int(input("Entre com sua idade: "))

print(nome, " tem ", idade, " anos. ")
print(f"{nome} tem {idade} anos. ")

if idade >= 60:
    print(f"{nome} já pode pagar 1/2 ingresso no cinema! ")
else:
    print(f"Parabéns {nome}! Você ainda é jovem!! ")

print("Acabou o programa! ")
