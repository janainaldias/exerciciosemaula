def maior(*num):
    cont=maior=0
    for valor in num:
        print(f'{valor}', end=' ')
        if cont==0:
            maior=valor
        elif valor>maior:
            maior=valor
        cont+=1
    print(f'\nForam informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}')

#Programa principal
maior(2,9,4,5,7,1)
maior(4,7,0)
maior(1,2)