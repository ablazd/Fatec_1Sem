compra = float(input("Entre com o total da compra: "))

if compra <= 1000:
    valor = compra - (compra * 10/100)
    print(f"Com desconto de 10% você pagará: {valor}")
elif (compra > 1000) and (compra <= 5000):
    valor = compra - (compra * 20/100)
    print(f"Com desconto de 20% você pagará: {valor}")
else:
    valor = compra - (compra * 30/100)
    print(f"Com desconto de 30% você pagará: {valor}")
