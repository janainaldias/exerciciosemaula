from MinhasFuncoes import*

'''# Exercício 1
print('Calculo das àreas de figuras geométricas:')
escolha=int(input('1. Círculo \n2. Triângulo \n3. Retangulo \nEscolha uma opção: '))

if escolha==1:
    raio=float(input('Informe o raio: '))
    area=calcula_area_circulo(raio)
    print(f'Àrea do círculo: {area:.2f}')
elif escolha==2:
    base=float(input('Informe a base: '))
    altura=float(input('Informe a altura: '))
    area=calcula_area_triangulo(base, altura)
    print(f'Àrea do triângulo: {area:.2f}')
elif escolha == 3:
    base=float(input('Informe a base: '))
    altura=float(input('Informe a altura: '))
    area=calcula_area_retangulo(base,altura)
    print(f'Àrea do retângulo: {area:.2f}')
else:
    print('Opção inválida.')'''

'''#Exercício 2,3,4
linhas=int(input('Informe a quantidade de linhas da matriz: '))
colunas=int(input('Informe a quantidade de colunas da matriz: '))
intervalo_inicial=int(input('Informe o intervalo inicial: '))
intervalo_final=int(input('nforme o intervalo final: '))

#Exercício 2
m=gera_matriz_aleatoria(linhas, colunas, intervalo_inicial, intervalo_final)
print(f'Matriz gerada: {m}')

if len(m)==len(m[0]):
    print(f'Traço da matriz gerada: {calcula_traco_matriz(m)}')
else:
    print('Não é possível calcular o traço pois não é uma quadrada.')'''

'''# Exercício 3
a=gera_matriz_aleatoria(linhas,colunas,intervalo_inicial,intervalo_final)
b=gera_matriz_aleatoria(linhas,colunas,intervalo_inicial,intervalo_final)

if len(a)==len(b) and len(a[0])==len(b[0]):
    print(f'Matriz A={a} \nMatriz B: {b} \nMatriz C (A+b)= {soma_matrizes(a,b)}')
else:
    print('As matrizes não tem a mesma ordem.')'''

# Exercício 4
'''m1=gera_matriz_aleatoria(linhas,colunas,intervalo_inicial,intervalo_final)
constante=int(input('Informe a constante que multiplicará a matriz gerada: '))
print(f'Matriz gerada: {m1} \nMatriz C (M1 * Constante)= {multiplica_matriz_por_constante(m1, constante)}')
'''

# Exercício 5
cadastro=obtem_dados_funcionario()
print(retorna_num_hom_mul(cadastro))
