def fatorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fatorial(n-1)

lista=[0,1,2,3,4,5,6]

for valor in lista:
    print(fatorial(valor))