# Exercício 4 - Aula 8

from random import choice

n1 = input('Primeiro aluno: ')
n2 = input('Segundo aluno: ')
n3 = input('Terceiro aluno: ')
n4 = input('Quarto aluno: ')

lista = [n1, n2, n3, n4]

escolhido = choice(lista)

print('O aluno esciolhido foi {}'.format(escolhido))