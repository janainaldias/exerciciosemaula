# Exercício 2 - Aula 19

''' Modo 1 - funciona mas não é o mais otimizado.
num = cont = soma = 0
while num!=999:
    soma+=num
    cont+=1
    num=int(input('Digite um número ou 999 para parar: '))
print(f'Você digitou {cont} números e a soma entre eles {soma}')

''' # Modo 2 - funciona e é mais otimizado.
n = s = c = 0
while True:
    n=int(input('Digite um número ou 999 para parar: '))
    if n==999:
        break
    c+=1
    s+=n
print(f'Você digitou {c} números e a soma entre eles {s}')
#'''