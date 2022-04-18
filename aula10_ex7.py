# Exercício 7 - Aula 10 : Atividade I

print('-*'*20)
print('1) Programador de sistemas \n 2) Analista de sistemas \n 3) Analista de banco de dados')
print('-*'*20)

salario=float(input('Digite o salário do funcionário: R$ '))
cargo=float(input('Digite o cargo do funcionario: '))

if cargo< 1 or cargo>3:
    print('Cargo inválido!')
elif cargo == 1:
    salario *= 1.3
    print('Novo salário R${:.2f} '.format(salario))
elif cargo == 2:
    salario *= 1.2
    print('Novo salário R${:.2f}'.format(salario))
else:
    salario *= 1.15
    print('Novo salario R${:.2f}')