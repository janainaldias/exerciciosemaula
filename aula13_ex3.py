# Exercício 3 - Aula 13

soma=0
cont=0

for c in range(1, 501):
    if c%3==0:
        if c%2!=0:
            soma+=c # soma=soma+c
            cont+=1 # cont=cont+1
print('A soma de todos os {} valores solicitados é {}'.format(cont,soma))