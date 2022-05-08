def exibirMensagem(): # Declarando uma função
    print('Python é fácil')

exibirMensagem() # Chamando a execução da função, sem isso a função não é executada

def exibirMensagemBoasVindas(pessoa, mensagem): # Função com passagem de parâmentro
    print(f'{mensagem}, {pessoa}')

exibirMensagemBoasVindas('Janaina', 'Bem-vinda') 

exibirMensagemBoasVindas() # mensagem de erro de falta de parâmentos necessários na função

def exibirMensagemBoasVindas(pessoa='Fulano', mensagem='Bem-vindo'):
    print(f'{mensagem}, {pessoa}')

exibirMensagemBoasVindas()