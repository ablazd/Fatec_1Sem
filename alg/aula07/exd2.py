sPeso = 0
sAlt = 0
maiorImc = 0
for i in range(1, 6):
    peso = float(input(f"Entre com o {i}o peso em quilogramas: "))
    alt = float(input(f"Entre com a {i}a altura em metros: "))
    sPeso = sPeso + peso
    sAlt = sAlt + alt
    imc = peso / (alt + alt)
    if maiorImc == 0:
# if i == 1: (outra opção)
        maiorImc = imc
        menorImc = imc
        if imc > maiorImc:
            maiorImc = imc
        if imc < menorImc:
            menorImc = imc
mediaPeso = sPeso / 5
mediaAlt = sAlt / 5
print(f"A media do peso das 5 pessoas é {mediaPeso}")
print(f"A media da altura das 5 pessoas é {mediaAlt}")
print(f"O menor IMC é {menorImc:5.2f}")
print(f"O maior IMC é {maiorImc:5.2f}")
