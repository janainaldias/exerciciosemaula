# Exercício 10 - Aula 19

estatura = float(input("Estatura do aluno: "))
 
'''Como não há nenhuma estatura a ser comparada, neste momento, o primeiro
aluno tem a maior e a menor estatura'''
menor = estatura
maior = estatura
 
soma_estatura = 0
soma_estatura += estatura
cont = 1
 
while True:
    estatura = float(input("Estatura do aluno: "))
    if estatura < 0:  # Quando estatura menor que zero, laço será interrompido
            break
    
    if estatura < menor:
        menor = estatura
    elif estatura > maior:
        maior = estatura
    
    # Conta quantas estaturas foram informadas
    cont += 1
    # Acumula as estaturas informadas
    soma_estatura += estatura
    # cont e soma_estatura serão usadas para calcular a média
 
media = soma_estatura / cont
print("{}m é a maior estatura. \n {}m é a menor estatura. \n média das estaturas = {:.2f}m".format(maior, menor, media))