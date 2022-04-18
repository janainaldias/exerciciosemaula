# Exercício 2 - Aula 10 : Atividade I

r1=float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

if r1<r2+r3 and r2<r1+r3 and r3<r1+r2:
    print('Os segmentos acima PODEM FORMAR um triângulo')
    if r1==r2 and r2==r3 and r3==r1:
        print('EQUILÁTERO')
    elif r1!=r2 and r1!=r3 and r2!=r1:
        print('ESCALENO!')
    else:
        print('ISOSCELES')
else:
    print('Os segmentosacima NÃO PODEM forma um triângulo')