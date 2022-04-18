# Exercício 1 - Aula 8

casa = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: '))
anos = int(input('Quantos anos de financiamento: '))

prestacao=casa/(anos*12)
minimo=salario*0.30

print('Para pagar uma casa de R${:.2f} em {} anos'.format(casa,anos))
print('A prestação será de R$ {:.2f}'.format(prestacao))

if prestacao <= minimo:
	print('Empréstimo pode ser CONCEDIDO!')
else:
	print('Empréstimo NEGADO!')
