# Exercício 2 - Aula 19

num = cont = soma = 0

num=int(input('Digite um número ou 999 para parar: '))

while num!=999:
    soma+=num
    cont+=1
    num=int(input('Digite um número ou 999 para parar: '))
print(f'Você digitou {cont} números e a soma entre eles e a soma entre eles {soma}')