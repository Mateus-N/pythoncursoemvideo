def leiaint (frase) :
    while True :
        try :
            valor = int ( input (frase))
        except :
            print ('Erro! valor inválido.')
        else :
            break
    return valor


def leiareal (frase) :
    while True :
        try :
            valor = float ( input (frase))
        except :
            print ('Erro! valor inválido.')
        else :
            break
    return valor


n = leiaint ('Digite um número inteiro: ')
r = leiareal ('Digite um número real: ')
print (f'Você digitou o número inteiro {n} e o número real {r}')
