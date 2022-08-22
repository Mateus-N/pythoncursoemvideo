def leiaint (frase) :
    ok = False
    valor = 0
    while ok == False :
        n = str ( input (frase))
        if n.isnumeric() :
            valor = int (n)
            ok = True
        else:
            print ('ERRO! Digite um número inteiro válido.')
    return valor


n = leiaint ('Digite um número: ')
print (f'Você digitou o número {n}')
