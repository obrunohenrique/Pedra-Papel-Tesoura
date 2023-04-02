from time import sleep
from random import choice

opcoes = 'pedra', 'papel', 'tesoura'
pc = choice(opcoes)
print('Escolha uma opção abaixo:\nPedra\nPapel\nTesoura')
user = str(input('Qual a sua escolha: ')).strip().lower()
print('PROCESSANDO...')
sleep(1)
print('Eu escolhi {} e você {}'.format(pc, user))
if pc == user:
    print('Deu empate, vamos tentar de novo.')
elif pc == 'pedra' and user == 'papel':
    print('Parabéns, você venceu!')
elif pc == 'papel' and user == 'tesoura':
    print('Parabéns, você venceu!')
elif pc == 'tesoura' and user == 'pedra':
    print('Parabéns, você venceu!')
else:
    print('Você perdeu, tente novamente!')
