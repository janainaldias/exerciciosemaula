print('## Programa de emprestimos ## \n Responda: 0 - Não e 1- Sim')
nomeNegativado = int(input('Possui nome negativado?'))

if nomeNegativado == 1:
    print('Não pode realizar o emprestimo.')
else:
    carteiraAssinada = int(input('possui carteira assinada? '))
    if carteiraAssinada == 0:
        print('Não pode realizar o emprestimo')
    else:
        possuiCasaPropria = int(input('Psossui casa própria? '))
        if possuiCasaPropria == 0:
            print('Não pode realizar o empréstimo.')
        else:
            print('Concede o empréstimo')

            