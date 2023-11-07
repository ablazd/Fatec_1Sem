def segundos(h, m, s):
    return (h * 3600 + m * 60 + s)


hora = int(input("Digite a hora: "))
minutos = int(input("Digite os minutos: "))
seg = int(input("Digite os segundos: "))


print(f"O total de segundos é {segundos(hora, minutos, seg)}")
