# Exercício 4 - Aula 4

sal_base=float(1500)
comissao=float(200)

corretor= input('Digite o nome do corretor: ')
qtde_vendas = int(input('Informe a quantide de imóveis vendidos: '))
total_vendas = float(input('Informe o valor total de vendas do corretor R$'))

sal_final = sal_base + (comissao*qtde_vendas) + (total_vendas*0.05)

print('Salario final do corretor {} é de R${:.2f}.'.format(corretor,sal_final))