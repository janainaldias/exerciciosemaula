# Exercício 4 - Aula 5

nome= input('Digite seu nome completo ')
maiuscula=nome.upper()
print('Seu nome em letras maiúsculas é {}'.format(maiuscula))
minuscula = nome.lower()
print('Seu nome em letras minúsculas é {}'.format(minuscula))
sem_espaco=len(nome)-nome.count(' ')
print('Seu nome tem {} letras.'.format(sem_espaco))
primeiro= nome.find(' ')
print("Seu primeiro nome tem {} letras".format(primeiro))