# Exercício 2 - Aula 10 : Atividade I

preco=float(input('Preço das compras: R$'))

print('Formas de pagamento: \n 1) à vista dinheiro ou cheque \n 2) à vista vista cartão \n 3) 2x no cartão')
opcao = int(input('Qual é a opção?'))

if opcao == 1:
    total = preco - (preco*10/100)
elif opcao == 2:
    total = preco - (preco*5/100)
elif opcao == 3:
    total= preco

print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco, total))