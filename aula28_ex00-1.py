from aula28_ex00 import *

escolha=int(input('1.Soma \n2.Substração \n3.Divisão \n4.Multiplicação \n5. Todas as operações\nEscolha uma das opções: '))

num1=int(input('Digite o 1º número: '))
num2=int(input('Digite o 2º número: '))

if escolha<0 or escolha>5:
    print('Opção inválida.')
elif escolha==1:
    s=soma(num1,num2)
    print(f'A soma entre os dois números é {s}')
elif escolha==2:
    sb=subtracao(num1,num2)
    print(f'A substração entre dois números é {sb}')
elif escolha==3:
    d=divisao(num1,num2)
    print(f'A divisão entre dois números é igual {d}')
elif escolha==4:
    m=multiplicacao(num1,num2)
    print(f'A multiplicação entre dois números é igual {m}')
elif escolha==5:
    c=calculadora(num1,num2)
    print(f'Soma={c[0]}, Subtração={c[1]}, Divisão={c[2]:.2f} e Multiplicação={c[3]}')
    