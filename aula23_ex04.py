termo=int(input('Informe o 1º termo da P.A. '))
num_termos=int(input('Informe o número de termos da P.A. '))
razao=int(input('Informe a razão da P.A. '))
pa = [termo]

termo_anterior=termo

for x in range(num_termos-1):
    termo_atual=termo_anterior+razao
    pa.append(termo_atual)
    termo_anterior=termo_atual
print(pa)

soma=sum(pa)

print(f'Soma dos elementos da PA = {soma}')
