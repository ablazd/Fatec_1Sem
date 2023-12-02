def eh_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True


def contar_primos_ate_n(n):
    count_primos = 0
    for i in range(n + 1):
        if eh_primo(i):
            count_primos += 1
    return count_primos


Y = int(input("Entre com o valor de acordo com o RA: "))
valor = Y * 2 + 5

eh_primo_valor = eh_primo(valor)
print(f"{valor} é primo? {eh_primo_valor}")

quantidade_primos = contar_primos_ate_n(valor)
print(f"Quantidade de primos até {valor}: {quantidade_primos}")

lista_primos = [i for i in range(valor + 1) if eh_primo(i)]
soma_primos = sum(lista_primos)

print(f"Lista de primos: {lista_primos}")
print(f"Valor da Soma de Todos os Números: {soma_primos}")
