# Exercício 3 - Aula 19

resp='S'
soma=quant=media=maior=menor=0

while resp in 'S':
    num=int(input('Digite um número: '))
    soma+=num
    quant+=1
    if quant == 1:
        maior=menor=num
    else:
        if num>maior:
            maior=num
        if num< menor:
            menor=num
    resp=input('Quer continuar [S/N]? ').upper().strip()
media=soma/quant

print(f'Você digitou {quant} números e a média foi {media}')
print(f'O maior valor foi {maior} e o menor valor foi {menor}')
