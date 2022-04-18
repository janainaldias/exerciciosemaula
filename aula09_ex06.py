# Exercício 1 - Aula 9

print('Grandezas Elétroicas')
print('1. Tensão (em Volt')
print('2. Resistência (em Ohm)')
print('3. Corrente (em Ampére)')

op=int(input('Qual grandeza deseja calcular? '))

if op< 1 or op>3:
    print('Opção inválida.')
elif  op ==1:
    R=float(input('Digite o valor da corrente em Ohm: '))
    i = float(input('Digite o valor da corrente em Ampére: '))
    U = R * i
    print('R = {:.2f}'.format(U))
elif op == 2:
    U = float(input('Digite o valor da tensão em Volts: '))
    i = float(input('Digite o valor da corrente em Ampére'))
    R = U/i
    print('R = {:.f}'.format(R))
else:
    U = float(input('Digite o valor de tensão em Volt: '))
    R = float(input('Digite o valor da corrente em Ohm: ' ))
    i= U/R
    print('i = {:.2f}')