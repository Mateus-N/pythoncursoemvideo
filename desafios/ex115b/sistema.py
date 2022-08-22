from lib.interface import *
from lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivoexiste (arq) :
    criararquivo (arq)


while True :
    resposta = menu (['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])
    if resposta == 1 :
        # Opção de listar o conteúdo de um arquivo!
        lerarquivo (arq)
    elif resposta == 2 :
        # Opção de cadastrar uma nova pessoa.
        cabeçalho ('NOVO CADASTRO')
        nome = str ( input ('Nome: '))
        idade = leiaint ('Idade: ')
        cadastrar (arq, nome, idade)
    elif resposta == 3 :
        cabeçalho ('Saindo do sistema... Até logo!')
        break
    else :
        print ('\033[31mERRO! Digite uma opção válida!\033[m')
    sleep (2)
