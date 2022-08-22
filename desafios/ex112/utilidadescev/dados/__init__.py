def leiadinheiro (frase) :
    valido = False
    valor = 0
    while not valido :
        numero = str ( input (frase)).replace(',', '.').strip()
        if numero.isalpha() or numero == '' :
            print (f'ERRO! "{numero}" é um preço inválido.')
        else:
            valor = float (numero)
            valido = True
    return valor
