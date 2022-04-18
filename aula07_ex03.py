# Exercício 3 - Aula 7

salario = float(input('Qual é o salario do funcionario? R$ '))
if salario <=1250:
    novo=salario+(salario*0.15)
else:
    novo=salario+(salario*0.10)

print('Quem ganahava R${:.2f} passa a ganhar R${:.2f} agora'.format(salario, novo))