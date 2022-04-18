'''
Exercício 6 - Aula 13

1 2 3 4 5 6 7 8 9 10 [1]
10 15 20 15 30 ... [5]
'''

primeiro=int(input('Termo: '))
razao=int(input('Razão: '))

decimo=primeiro+(10-1)*razao

for c in range(primeiro, decimo+razao, razao):
    print('{}'.format(c), end='->')
print('Acabou')
