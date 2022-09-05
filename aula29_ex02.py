def horario(hora, minuto):
    b=hora/12

    if b<=1:
        h=str(hora)
        print(f'Sua hora: {h}:', end='')
    elif b>1 and b<=2:
        h= str(hora-12)
        print(f'Sua hora: {h}:', end='')

    if b<=1 and minuto<=60:
        print(f'{minuto} a.m')
    elif b>1 and minuto<=60:
        print(f'{minuto} p.m')
    
while True:
    print('Digite 999 para sair')
    h=int(input('Informe a hora: '))
    if h==999:
        break
    m=int(input('Informe os minutos: '))
    horario(h,m)
