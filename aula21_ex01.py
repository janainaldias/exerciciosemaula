'''
Maior valor: 78
Menor valor: -52
Lista de elementos pares: [12, -2, 4, 8, 78, 36, 2, 12, 12, -52]
Número de ocorrências do primeiro item: 3
Média dos elementos: -3.452191512695258
Somatório dos valores negativos: -71
'''

lista = [12, -2, 4, 8, 29, 45, 78, 36, -17, 2, 12, 8, 3, 3,-52]
maiovalor=lista[0]
menorvalor=lista[0]
listaPares=[]
ocorrencia=0
mediaElementos=0
somaNegativo=0

for index in range(0,len(lista)):
    #Maior valor
    if maiovalor<lista[index]:
        maiovalor=lista[index]
    #Menor valor
    if menorvalor>lista[index]:
        menorvalor=lista[index]
    #Lista números pares
    if lista[index]%2==0:
        listaPares.append(lista[index])
    # Ocorrência primeiro elemento
    if lista[index]==lista[0]:
        ocorrencia+=1
    #Somatório para média
    mediaElementos+=lista[index]
    #Soma números negativos
    if lista[index]<0:
        somaNegativo+=lista[index]

# Média
mediaElementos/=len(lista)

print(f'Maior valor: {maiovalor}')
print(f'Menor valor: {menorvalor}')
print(f'Lista de números pares: {listaPares}')
print(f'Número de ocorrências do primeiro elemento: {ocorrencia}')
print(f'Média elementos: {mediaElementos}')
print(f'Elementos negativos: {somaNegativo}')
