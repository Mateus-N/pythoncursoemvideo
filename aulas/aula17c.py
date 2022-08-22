valores = []
while True:
    valores.append( int ( input ('Digite um valor: ')))
    while True:
        continuar = str ( input ('Quer continuar [S/N] ? '))[0]
        if continuar in 'sSnN':
            break
    if continuar in 'nN':
        break
