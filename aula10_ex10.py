# Exercício 10 - Aula 10 : Atividade I

nome=input('Digite seu nome completo: ').strip()

divide_nome=nome.split()

print('Muito prazer em te conhecer! \n Seu primeiro nome é {} e seu último nome é {}'.format(divide_nome[0], divide_nome[len(divide_nome)-1]))
