num=[]
for n in range(0,10):
    num.append(n**2)
print(num)

# Listas comprimidas
lista1= [x**2 for x in range(10)] # inserindo na lista os números entre 0 e 10 elevados ao quadrado
print(lista1)

lista2=[x for x in range(1,20) if x%2==0] # inserindo na lista os números pares no interalo de 0 a 20
print(lista2)

lista3=[i for i in "HACKATHON" if i in ['A', 'E', 'I', 'O', 'U']] # inserindo as vogais de uma string em uma lista
print(lista3)

lista4=[1,2,3] 
lista4=[i**3 for i in lista4] # atribuir novos valores aos elementos da lista através de uma operação.
print(lista4)