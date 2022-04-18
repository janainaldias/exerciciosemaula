# Exercício 5 - Aula 8

from random import shuffle

n1 = input('Primeiro aluno: ')
n2 = input('Segundo aluno: ')
n3 = input('Terceiro aluno: ')
n4 = input('Quarto aluno: ')

lista = [n1, n2, n3, n4]

print('Os alunos que compõe a turma são {}'.format(lista))

shuffle(lista)

#print('A ordem de apresentação será {}'.format(lista))

print('A ordem de apresentação será {}, {}, {}, {}'.format(lista[0],lista[1],lista[2],lista[3]))