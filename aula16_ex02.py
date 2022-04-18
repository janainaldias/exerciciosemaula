# Exercício 2 - Aula 16

soma=0

medicamento=input('Medicamento: ')
preco=float(input('R$: '))

maisbarato=medicamento
menorpreco=preco

soma+=preco

for x in range(4):
    medicamento=input('Medicamentos: ')
    preco=float(input('R$:'))
    if preco<menorpreco:
        menorpreco=preco
        maisbarato=medicamento
    soma+=preco
media=soma/5

print(f'{maisbarato} é o médicamento mais barato e custa R$ {menorpreco}. \n Média dos preços: {media}')

