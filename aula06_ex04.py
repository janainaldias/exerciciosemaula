# Exercício 4 - Aula 6

distancia = float(input('Qual a distância da sua viagem? '))
preco=distancia*0.5 if distancia<=200 else distancia*0.45
print('E o preço da sua passagem será de R${:.2f}'.format(preco))