# Exercício 4 - Aula 7

r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo  segmento: '))
r3 = float(input('Terceiro segmento: '))
# Cada um dos segmentos tem que ser menor que a soma dos outros dois
# Funciona 3 3 3 ; 9 7 8
# Não funciona 2 3 e 6


if r1<r2+r3 and r2<r1+r3 and r3<r1+r2:
    print('Os segmentos acima PODEM FORMAR triângulo!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR trinângulo!')