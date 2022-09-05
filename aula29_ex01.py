def somaImposto(taxaImposto,custo):
    return (0.01*taxaImposto)*custo+custo

taxa=int(input('Digite a taxa de imposto do produto: '))
valor=int(input('Digite o custo do produto: '))
print(f'Qual o valor do produto com o imposto: {somaImposto(taxa,valor)}')