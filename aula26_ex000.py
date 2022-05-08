# Função para realizar a soma dos elementos de uma lista

def somarElementosLista(inteiros):
    soma=0
    for valor in inteiros:
        soma+=valor
    return soma

lista=[3,4,6,9,10,23,13]

print(somarElementosLista(lista))