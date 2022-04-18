# Exercício 3 - Aula 15
somaidade=0
maioridadehomem=0
nomemaisvelho= ''
mulhermenor=0
mediaidade=0

for p in range(1,5):
    nome=input('Nome: ').strip()
    idade=int(input('Idade: '))
    sexo=input('Sexo [F/M]: ').strip().upper()
    somaidade+=idade

    if p==1 and sexo in 'M':
        maioridadehomem=idade
        nomemaisvelho=nome

    if sexo in 'M' and idade>maioridadehomem:
        maioridadehomem=idade
        nomemaisvelho=nome

    if sexo in 'F' and idade<20:
        mulhermenor+=1

mediaidade=somaidade/4

print('A média de idade do grupo é de {} anos.'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}.'.format(maioridadehomem,nomemaisvelho))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(mulhermenor))