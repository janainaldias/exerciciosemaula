# Resolvido utilizando a estrutura de dados tupla
'''
num=((int(input('Digite um número:')), int(input('Digite um outro número:')), 
int(input('Digite mais um número:')), int(input('Digite o último número:'))))

if 9 in num:
    print(f'O valor apareceu {num.count(9)} vezes')
else:
    print('O número 9 não foi informado.')

if 3 in num:
    print(f'O número 3 foi digitado na {num.index(3)+1}ª posição.')
else:
    print('O número 3 não foi informado.')

for n in num:
    if n%2==0:
        print(n, end=' ')'''

# Resolvido utilizando a estrutura de dados lista

num=[]

for n in range(0,4):
    num.append(int(input('Digite um número:')))

if 9 in num:
    print(f'O valor apareceu {num.count(9)} vezes')
else:
    print('O número 9 não foi informado.')

if 3 in num:
    print(f'O número 3 foi digitado na {num.index(3)+1}ª posição.')
else:
    print('O número 3 não foi informado.')

for n in num:
    if n%2==0:
        print(n, end=' ')

