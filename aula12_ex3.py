# Exercício 3 - Aula 12

alt1=float(input('Digite a estatura da 1ª pessoa: '))
alt2=float(input('Digite a estatura da 2ª pessoa: '))
alt3=float(input('Digite a estatura da 3ª pessoa: '))

mais_alto= alt1
est_mediana=alt1
mais_baixo=alt1

if alt1> alt2 and alt1>alt3:
    mais_alto=alt1
    if alt2>alt3:
        est_mediana = alt2
        mais_baixo = alt3
    else:
        est_mediana = alt3
        mais_baixo = alt2
elif alt2>alt1 and alt2> alt3:
    mais_alto=alt2
    if alt1> alt3:
        est_mediana = alt1
        mais_baixo = alt3
    else:
        est_mediana=alt3
        mais_baixo=alt1
else:
    mais_alto = alt3
    if alt1 > alt2:
        est_mediana = alt1
        mais_baixo = alt2
    else:
        est_mediana = alt2
        mais_baixo = alt1

print('Mais alto: {}m, Mediano {}m e Mais baixo: {}m'.format(mais_alto, est_mediana, mais_baixo))