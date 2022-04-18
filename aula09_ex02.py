# Exercício 2 - Aula 9

num = int(input('Digite um número inteiro: '))

print(''' Escolha uma das bases para conversão: \n [1] converter para binário \n [2] converter para octal \n [3] converter para hexadecimal''')

opcao=int(input('Sua opção: '))

if opcao == 1:
    print('{} convertido para binário é igual a {}'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('{} convertido para octal é igual a {}'.format(num,oct(num)[2:]))
elif opcao == 3:
    print('{} convertido para hexadecimal é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Opção inválida. Tente novamente.')    