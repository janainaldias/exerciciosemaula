from random import shuffle, choice

rifa=[]

while True:
    nome=input('Informe o nome do comprador: ')
    rifa.append(nome)
    resp=input('Deseja continuar [S/N]? ')
    if resp.upper()=='N':
        break

shuffle(rifa)
sorteado=choice(rifa)

print(f'O ganhador da rifa foi o {sorteado}')
