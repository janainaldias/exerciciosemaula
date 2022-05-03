n = int(input('Digite um número ímpar, maior que 1: '))

if n<=1 or n%2==0:
    print('Número informado não atende os críterios defindos.')
else:
    l=[]
    for x in range(n):
        num=int(input('Digite um número maior ou igual a zero:'))
        l.append(num)

centro=int(len(l)/2)
elementocentro=l[centro]
fatorial=1

# 1*2*3*4*5=120
for n in range(2, elementocentro+1):
    fatorial*=n
print(f'Lista: {l}')
print(f'O elemento do centro da lista {elementocentro} e seu fatorial é igual {fatorial}')