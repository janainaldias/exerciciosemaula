def escreva(msg):
    tam=len(msg)+4
    print('~'*tam)
    print(f'{msg}')
    print('~'*tam)

# Programa principal
# Mensagem fixa no código
escreva('Na aula de hoje estudamos funções em Python')
escreva('Turma Inf 9 - SENAC - SCS')
# Mensagem digitada do usuário 
escreva(input('Digite uma frase: '))