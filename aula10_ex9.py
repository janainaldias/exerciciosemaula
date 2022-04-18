# Exercício 9 - Aula 10 : Atividade I

login = input('login:')
senha = int(input('senha:'))

if (login == 'souza' and senha == '1234') or (login =='pereira' and senha =='54321'):
    print("Seja bem vindo!")
else:
    print('Usuário e senha não conferem.')