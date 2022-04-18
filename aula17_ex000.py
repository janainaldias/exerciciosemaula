#Variável de entrada que vai receber a frase
frase=input('Digite a frase: ')
 
#Variável de entrada que vai receber o caractere a ser contado
caractere=input('Digite o caractere que busca: ')
 
#Iniciando a variável que será usada como contador de caracteres
qtde=0
 
#Estrutura de repetição do for que inicia em c e percorre à variável frase
for c in frase:
 
#Estrutura condicional que testa se o caractere armazenado em c na execução atual é igual ao caractere que deve ser contado
    if c.lower()==caractere.lower():
 
#Expressão que adiciona 1 a variável quantidade quando a condição anterior é atendida
        qtde+=1
 
#Imprime em tela a quantidade de vezes que o caractere procurado foi encontrado na frase
print(f'O caractere apareceu {qtde} vezes na frase.')