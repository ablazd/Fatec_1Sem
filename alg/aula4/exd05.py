salario = float(input('Digite o salário atual: R$'))
aumento = int(input('Digite o aumento em porcentagem: '))
novo_salario = salario * ((salario*aumento) /100)
print('O novo salário é R$', novo_salario)
