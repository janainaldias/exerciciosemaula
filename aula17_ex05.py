total=totmil=menor=cont=0
barato=' '
while True:
    produto=str(input('Nome do produto: '))
    preco=float(input('Preço R$: '))
    cont+=1
    total+=preco
    if preco>1000:
        totmil+=1
    if cont==1 or preco<menor:
        menor=preco
        barato=produto
    resp=' '
    while resp not in 'SN':
        resp=input('Quer continuar [S/N]?').strip().upper()
    if resp=='N':
        break
print(f'O total das compras foi R${total:.2f}')
print(f'Temos {totmil} produtos custando mais de R$1000,00.')
print(f'O produto mais barato foi {produto} que custa R${menor:.2f}')