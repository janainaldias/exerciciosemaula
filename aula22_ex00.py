# Listas / Vetpres
lista=[ 'Maria', 'Janaina', 'José', 'Carlos']
listaa=['José', 'Pedro']

for n in range(0, len(lista)): # Percorrer a lista
   print(lista[n]) # Imprimir os elementos da lista

lista.append('Jorge') # Inserir novo item na última posição da lista
lista.insert(0,'Jorge') # Inserir novo item na posição desejada da lista de acordo com o índice informado

lista.sort() # Ordenar a lista em ordem crescente de modo permanente
lista.sort(reverse=True) # Ordenar a lista em ordem decrescente de modo permanente

sorted(lista) # Obter uma CÓPIA ordenada de uma lista

del lista[-1] # Remover um item de acordo com um índice informado
lista.remove('Janaina')  # Remover um item de valor determinado
lista.pop() # Remover um item de acordo com um índice informado ou o último se vazio

lista.clear() # Limpar lista.

listaa=lista # Vincular uma lista na outra.

listaa=lista[:] # Copiar itens de uma lista para outra.

lista.extend(listaa) # Adicionar uma lista na outra.

print(lista.count('José')) # Contar quantas vezes esse valor aparece na lista.

print(len(lista)) # Tamanho da lista

print(lista.index('Janaina')) # Índice na qual o valor informado está na lista.

for indice, nome in enumerate(lista): # Imprimir o índice e o valor de cada item da lista.
    print(f'{nome} está armazenado no índice {indice}')


# Lista composta / Matriz

a=[[2,1,-5],
   [3,7,0],
   [6,4,8]]

print(a[0][0], a[0][1], a[0][2]) # Imprimir os elementos de uma linha
print(a[0][0], a[1][0], a[2][0]) # Imprimir os elementos de uma coluna

# Soma de todos os item da matriz
soma_a=0
lin=len(a)
col=len(a[0])

for i in range(lin):
    for j in range(col):
        soma_a+=a[i][j]

print(soma_a)

# Impressão dos elementos da matriz
lin=len(a)
col=len(a[0])

for i in range(lin):
    print('|', end=' ')
    for j in range(col):
        print(a[i][j], end=' ')
    print('\n', end='')
    