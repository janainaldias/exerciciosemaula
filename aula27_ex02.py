def ficha(jog='Janaina', gol=0):
    print(f'O jogador {jog} fez {gol} gol(s) no campeonato.')

n=input('Nome do jogado: ')
g=int(input('Número de gols: '))

if g.isnumeric():
    g=int(g)
else:
    g=0

if n.strip()=='':
    ficha(gol=g)
else:
    ficha(n,g)

'''if type(g)==int:
    print('Sim')
else:
    print('Não')'''
