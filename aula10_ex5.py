# Exercício 5 - Aula 10 : Atividade I

numeroCamisa=int(input('Número de camisas: '))
valorCamisa = 12.5
valorFinal = numeroCamisas*valorCamisa
if numeroCamisa <=5:
    valorFinal=valorFinal*(1-3/100)
elif numeroCamisa<=10:
    valorFinal=valorFinal*(1-5/100)
else:
    valorFinal=valorFinal*(1-7/100)

print('Valor final: R$ {:.2f}'.format(valorFinal))

#print(f'Valor final: R$ {valorFinal:.2f}')