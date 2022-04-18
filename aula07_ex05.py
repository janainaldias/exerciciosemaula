# Exercício 5 - Aula 7

num1=float(input('Digite um número: '))
num2=float(input('Digite outro número: '))

print('\n1. Média ponderada, com pesos 2 e 3, respectivamente \n2. Quadrado da soma dos 2 números \n3. Cubo do menor número')
op=int(input('Escolha uma opção: '))

if op<1 or op>3:
    print('Opção inválida.')
elif op == 1:
    media = (num1*2+num2*3)/5
    print('Média ponderada calcilada: {:.2f}'.format(media))
elif op == 2:
    quadrado=(num1+num2)**2
    print('Quadrado da soma dos números: {:.2f}'.format(quadrado))
else:
    if num1<num2:
        cubo=num1**3
        print('{} é o menor e seu cubo é {} '.format(num1, cubo))
    else:
        cubo=num2**3
        print('{} é o menor e seu cubo é {}'.format(num2,cubo))    