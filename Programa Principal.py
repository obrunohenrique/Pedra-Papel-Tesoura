from time import sleep
from random import choice
from lib.interface import * 

linha()
print(f'{"Jokempô em Python"}'.center(40))
vitorias = empates = derrotas = 0
while True:
    opcoes = 'pedra', 'papel', 'tesoura'
    pc = choice(opcoes)
    cabecalho('Escolha uma opção abaixo:\na) Pedra\nb) Papel\nc) Tesoura')

    user = str(input('Qual a sua escolha: ')).strip().lower()
    if user == 'a' or 'pedra':
        user = 'pedra'
    elif user == 'b' or 'papel':
        user = 'papel'
    elif user == 'c' or 'tesoura':
        user = 'tesoura'

    cabecalho('PROCESSANDO...')
    sleep(1)
    print('Eu escolhi {} e você {}'.format(pc, user))
    if pc == user:
        print('Deu empate, vamos tentar de novo.')
        empates += 1
        reinicio
    elif pc == 'pedra' and user == 'papel':
        print('Parabéns, você venceu!')
        vitorias += 1
        reinicio
    elif pc == 'papel' and user == 'tesoura':
        print('Parabéns, você venceu!')
        vitorias += 1
        reinicio
    elif pc == 'tesoura' and user == 'pedra':
        print('Parabéns, você venceu!')
        vitorias += 1
        reinicio
    else:
        print('Você perdeu, tente novamente!')
        derrotas += 1
    repetir = str(input('Jogar novamente? [S/N]: ')).strip().lower()[0]
    if repetir == 'n':
        break

cabecalho('Realizando as Contagens...')
sleep(1)
print(f'O máximo de vitórias foi: {vitorias}')
print(f'O máximo de empates foi: {empates}')
print(f'O máximo de derrotas foi: {derrotas}')
