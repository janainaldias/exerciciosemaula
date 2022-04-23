# Exercício 8 - Aula 19

a = int(input('Digite a: '))
b = int(input('Digite b: '))
if a < b:
   soma = 0
   for x in range(a, b + 1):
      soma += x
   print('Soma dos inteiros no intervalo [{}, {}] é {}.'.format(a,b,soma))
else:
   print('ERRO: a deve ser maior que b.')