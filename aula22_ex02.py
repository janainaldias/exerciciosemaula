times=('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro',
'Flamengo',  'Vasco', 'Chapecoense', 'Atlético', 'Botafogo', 'Atlético-PR'
'Bahia', 'São Paulo', 'Fluminence', 'Sport Recife', 'Vitória', 'Coritiba',
'Avaí', 'Ponte Preta', 'Atlético-GO')

print(f'Cinco primeiros colocados {times[0:5]}')

print(f'Quatro últimos colocados {times[-4:]}')

clubes=times.index('Chapecoense')
print(f'A Chapecoense está na {clubes+1}ª posição')
