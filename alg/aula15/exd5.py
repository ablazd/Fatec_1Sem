def valorPagamento(valorPrestacao, atraso):
    valorTotal = 0
    if atraso == 0:
        valorTotal = valorPrestacao
    else:
        valorTotal = valorPrestacao + (valorPrestacao * 0.03) + (valorPrestacao * (0.001 * atraso))
    return valorTotal

relatorio = 0
contador = 0
while True:
    valor = float(input('Digite o valor da prestação: '))
    if valor == 0:
        print(f"Foram realizados {contador} pagamento(s) num total de R$ {relatorio:.2f}.")
        break
    dias = int(input('Digite o número de dias de atraso: '))
    print(f"Valor total a ser pago: R${valorPagamento(valor, dias):.2f}.")
    relatorio += valorPagamento(valor, dias)
    contador += 1
