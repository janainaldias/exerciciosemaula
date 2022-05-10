def soma(n1,n2):
    """
    Essa função realiza a soma entre dois números
    n1: espera receber um número inteiro
    n2: espera receber um número inteiro
    """
    soma=n1+n2
    return soma

def subtracao(n1,n2):
    subtracao=n1-n2
    return subtracao

def divisao(n1,n2):
    divisao=n1/n2
    return divisao

def multiplicacao(n1,n2):
    multiplicacao=n1*n2
    return multiplicacao

def calculadora(n1,n2):
   return soma(n1,n2), subtracao(n1,n2), divisao(n1,n2), multiplicacao(n1,n2)
   