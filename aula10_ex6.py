# Exercício 6 - Aula 10 : Atividade I

from random import randint

itens= ['Pedra', 'Papel', 'Tesoura']
computador = randint(0,2)
print('Suas opções são: [0] Pedra [1] Papel [2] Tesoura')

jogador=int(input('Qual sua jogada? '))

print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))

if computador == 0: # computador jogou PEDRA
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('Jogador vence')
    elif jogador == 2:
        print('Computador vence')
    else:
        print('Jogada inválida!')

if computador == 1: # computador jogou PAPEL
    if jogador == 0:
        print('Computador vence')
    elif jogador == 1:
        print('Empate')
    elif jogador == 2:
        print('Jogador vence')
    else:
        print('Jogada inválida!')

if computador == 2: # computador jogou TESOURA
    if jogador == 0:
        print('Jogador vence.')
    elif jogador == 1:
        print('Computador vencer.')
    elif jogador == 2:
        print('Empate.')
    else:
        print('Jogada inválida!')