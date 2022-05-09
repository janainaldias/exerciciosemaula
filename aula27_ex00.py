def escreve(msg):
    """
    Print de mesagem informada pelo usuário
    msg: entrada do usuário para programa
    """
    print('~')
    print(msg)
    print('~') 

#escreve(input('Digite uma frase: '))

#help(escreve) # 

def teste(b):
    b+=4 # Variável de escopo local
    c=2 # Variável de escopo local
    print(f'A dentro da função vale {a}')
    print(f'B dentro da função vale {b}')
    print(f'C dentro da função vale {c}')

#Programa principal
a=5 # Variável de escopo global
teste(a)
print(f'A fora da função vale {a}')
#print(f'B dentro da função vale {b}') # NameError: name 'b' is not defined
#print(f'C dentro da função vale {c}') # NameError: name 'c' is not defined