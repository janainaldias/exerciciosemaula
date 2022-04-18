sexo=input('Informe seu sexo [M/F]: ').strip().upper()
while sexo not in 'MF':
    sexo=input('Dados inválidos. Por favor, informe seu sexo [M/F]: ').strip().upper()
print('Sexo {} registrado com sucesso.'.format(sexo))