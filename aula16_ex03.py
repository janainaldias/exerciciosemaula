# Exercício 3 - Aula 16

'''for c in range(3,0,-1):
    senha = int(input("Senha: "))
    if senha == 123456:
        print("Olá, você. Seja bem-vindo ao nosso banco!")
        break
    elif senha != 123456:
        print("Senha incorreta! Você ainda tem {} tentativa(s).".format(c-1))
        if c==1:
            print("Sua senha foi bloqueada! Por favor, dirija-se a um de nossos caixas.")
            break'''

erros = 0
while erros < 3:
    senha = int(input("Senha: "))
    if senha == 123456:
        print("Olá, você. Seja bem-vindo ao nosso banco!")
        break
    else: # Houve erro
        erros += 1        # Ainda há tentativas
    if erros < 3:        # O comando "3 - erros" significa 3 tentativas - a quantidade de erros
        print("Senha incorreta! Você ainda tem {} tentativa(s).".format(3-erros))
    else:
       print("Sua senha foi bloqueada! Por favor, dirija-se a um de nossos caixas.")
       break
