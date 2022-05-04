from random import randrange

n=int(input('Informe o valor para N: '))

if n>0:
    l1=[randrange(1,11) for i in range(n)]
    l2=[randrange(1,11) for i in range(n)]

    l3=[]

    for i in range(n):
        l3.append(l1[i]+l2[i])

    print(f'L1 = {l1}')
    print(f'L2 =  {l2}') 
    print(f'L3 = {l3}')
else:
    print('Erro: N deve ser maior que 0')