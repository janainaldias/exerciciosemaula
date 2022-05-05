atletas=[]
tempo=[]

for x in range(3):
    nome=input('Informe o nome do nadador: ')
    tempos=float(input('Informe o tempo do nadador: '))
    atletas.append(nome)
    tempo.append(tempos)

indice_melhor=tempo.index(min(tempo)) # Imprime o índice do melhor tempo

indice_pior=tempo.index(max(tempo)) # Imprime o índice do pior tempo

media_tempos= sum(tempo)/len(tempo)

print(f'{atletas[indice_melhor]} tem o melhor tempo. ')
print(f'{atletas[indice_pior]} tem o pior tempo. ')
print(f'Média dos tempos: {media_tempos:.2f}. ')


