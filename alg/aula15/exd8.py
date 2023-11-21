import random

def jogarDados():
    dados = random.randint(2, 12)
    return dados

rodadaAtual = 1

while True:
    jogar = input(f'Rodada {rodadaAtual}: Jogar dados? (S/N) ').upper()
    if jogar == 'S':
        valorDado = jogarDados()
        if rodadaAtual == 1:
            if valorDado == 7 or valorDado == 11:
                print(f'Você tirou {valorDado}, um natural parabéns você venceu.')
                break
            if valorDado == 2 or valorDado == 3 or valorDado == 12:
                print(f'Você tirou {valorDado}, "Craps" você perdeu.')
                break
            else:
                print(f'Você tirou {valorDado}, marque seu ponto.')
                ponto = valorDado
        if rodadaAtual != 1 and valorDado == 7:
            print(f'Você tirou {valorDado}, você perdeu.')
            break
        if rodadaAtual != 1 and ponto == valorDado:
            print(f'Você tirou {valorDado}, parabéns você venceu.')
            break
        if rodadaAtual != 1:
            print(f'Você tirou {valorDado}.')
        rodadaAtual += 1
