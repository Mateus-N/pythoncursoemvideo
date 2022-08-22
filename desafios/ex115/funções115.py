from time import sleep
bancodedados = []


def linha () :
    print ('-'*50)


def titulo (texto) :
    linha ()
    print (f'{texto:^50}')
    linha ()


def leiaint (frase) :
    while True :
        try :
            valor = int ( input (frase))
        except :
            print ('Erro! valor inválido.')
        else :
            break
    return valor


def cadastro (nome, idade) :
    ficha = {}
    ficha['nome'] = str (nome)
    ficha['idade'] = int (idade)
    bancodedados.append (ficha.copy())
    print ('Cadastro efetuado com sucesso!')
    sleep (1.5)


def mostrarcadastro () :
    titulo ('PESSOAS CADASTRADAS')
    print (f'{"Nome":<35} Idade')
    linha ()
    sleep (1.5)
    for i in bancodedados :
        print (f'{i["nome"]:<35} {i["idade"]} anos')
    sleep (3)

