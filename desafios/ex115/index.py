import funções115


while True :
    funções115.titulo ('MENU PRINCIPAL')
    print ('1 - Ver pessoas cadastradas \n2 - Cadastrar nova pessoa \n3 - Sair do sistema')
    funções115.linha ()
    opção = funções115.leiaint ('Sua opção: ')

    if opção == 1 :

        funções115.mostrarcadastro ()

    elif opção == 2 :

        nome = str ( input ('Nome: '))
        idade = funções115.leiaint ('Idade: ')
        funções115.cadastro (nome, idade)
        
    elif opção == 3 :

        break

    else:

        print ('Opção inválida! Digite uma opção válida.')
