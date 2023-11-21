def verificarPositivo(num):
    if num > 0:
        return 'P'
    else:
        return 'N'

print(verificarPositivo(int(input('Digite um numero: '))))
