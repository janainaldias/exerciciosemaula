# Exercício 1 - Aula 7

ano = int(input('Que ano quer analisar?'))

if ano%4 == 0:
        print('O ano {}  é BISSEXTO'.format(ano))
else:
    print('O ano {} NÃO é BISSEXTO'.format(ano))