# Utilizando o print para retornar o valor ao usuário
def area (larg, comp):
    a=larg*comp
    print(f'A área de um terreno {larg}x{comp} é de {a}m²')

# Programa principal
print('Controle terrenos')
l=float(input('Largura (m): '))
c=float(input('Comprimento (m): '))
area(l,c)

# Utilizando o return para retornar o valor ao usuário
def areaII (larg, comp):
    a=larg*comp
    return a
# Programa principal
print('Controle terrenos')
l=float(input('Largura (m): '))
c=float(input('Comprimento (m): '))
print(f'A área de um terreno {l}x{c} é de {areaII(l,c)}m²')
