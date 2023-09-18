ano_n = int(input('Digite o ano de nascimento: '))
ano_at = int(input('Digite o ano atual: '))
idade_at = ano_at - ano_n
idade_meses = idade_at * 12
idade_dias = idade_at * 365
idade_semanas = idade_at * 53
print('A sua idade em anos é: ', idade_at)
print('A sua idade em meses é: ', idade_meses)
print('A sua idade em dias é: ', idade_dias)
print('A sua idade em semanas é: ', idade_semanas)
