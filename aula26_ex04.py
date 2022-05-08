from random import randint

def sorteia(lista):
    for cont in range(0,5):
        n= randint(1,10)
        lista.append(n)

def somaPar(lista):
    soma=0
    for valor in lista:
        if valor%2==0:
            soma+=valor
    print(f'Somando os valores pares de {lista}, temos {soma}')

numeros=list()
sorteia(numeros)
somaPar(numeros)