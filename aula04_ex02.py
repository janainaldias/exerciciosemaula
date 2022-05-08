# Exercício 2 - Aula 4

from math import sqrt

x1=float(input('Digite x1:'))
y1=float(input('Digite y1'))

x2=float(input('Digite x2:'))
y2=float(input('Digite y2:'))

d= sqrt((x2-x1)**2+(y2-y1)**2)

print('Distancia entre P1 e P2 é igual {:.2f}'.format(d))

p=((x2-x1)**2+(y2-y1)**2)**0.5

print('Distancia entre P1 e P2 é igual {:.2f}'.format(p))
