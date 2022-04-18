# Exercício 5 - Aula 9

nota1=float(input('Primeira nota: '))
nota2=float(input('Segunda nota: '))

media=(nota1+nota2)/2

print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.forma(nota1,nota2,media))

if 7> media >=5:
    print('O aluno está em recuperação.')
elif media < 5:
    print('O aluno está reprovado.')
else:
    print('O aluno está aprovado.')