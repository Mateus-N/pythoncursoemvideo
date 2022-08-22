def leiaint (frase) :
    while True :
        try :
            valor = int ( input (frase))
        except :
            print ('Erro! valor inválido.')
        else :
            break
    return valor


def linha (tam = 42) :
    print ('-' * tam)


def cabeçalho (txt) :
    linha ()
    print (txt.center(42))
    linha ()


def menu (lista) :
    cabeçalho ('MENU PRINCIPAL')
    for c, item in enumerate(lista) :
        print (f'\033[33m{c + 1}\033[m - \033[34m{item}\033[m')
    linha ()
    opc = leiaint ('\033[32mSua opção: \033[m')
    return opc
