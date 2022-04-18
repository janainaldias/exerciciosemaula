# Exercício 2 - Aula 8

largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))

area = largura * altura

print('Sua parede tem a dimensão de {}x{} e sua àrea é de {}m'.format(largura, altura, area))

tinta = area / 2

print('Para pintar essa parede, você precisará de {}l de tinta.'.format(tinta))
