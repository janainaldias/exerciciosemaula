listagem=('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.90, 'Estojo', 25, 'Transferidor', 4.20, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)

print('-'*40)
print('Valor dos Produtos:')
print('-'*40)
for l in range(0, len(listagem)):
    if l%2==0:
        print(f'{listagem[l]:.<30}', end='')
    else:
        print(f'{listagem[l]:.>7.2f}')
print('-'*40)