# Exercício 1 - Aula 6

from random import randint

computador=randint(0,5)

print('Vou pensar em um número entre 0 e 5, tente adinhar ...')

jogador = int(input('Em que número estou pensando? '))

if jogador == computador:
    print('PARABÉNS, você acertou!')
else:
    print('GANHEI, estava pensando no número {}, você errou!'.format(computador))