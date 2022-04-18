# Exercício 2 - Aula 6

velocidade = float(input('Qual é a velocidade atual do carro?'))

if velocidade > 80:
    print('Você foi multado! Excedeu a velocidade permitida!')
    multa = (velocidade-80)*7
    print('Você deve pagar uma multa de R${:.2f}'.format(multa))
else:
    print('Tenha um bom dia! Dirija com segurança!')