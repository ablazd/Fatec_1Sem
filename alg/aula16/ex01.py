cabecas = int(input("Digite a quantidade de cabeças a partir do seu RA: "))
pes = int(input("Digite a quantidade de cabeças a partir do seu RA: "))

total_cabecas = cabecas*2+5
total_pes = pes*3+7

coelho = (total_pes - total_cabecas * 2) / 2
if coelho < 0:
    coelho = coelho*-1
    pato = total_cabecas - coelho
    print(f"O total de patos é {pato} e o de coelhos é {coelho}.")
