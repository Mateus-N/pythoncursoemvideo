menu = 4
while menu == 4:
    n1=int(input('Digite o primeiro valor: '))
    n2=int(input('Digite o segundo valor: '))
    while 0<=menu<=3:
        print('O que você deseja fazer:\n [ 1 ] Somar\n [ 2 ] Multiplicar\n [ 3 ] Maior\n [ 4 ] Novos números\n [ 5 ] Sair do programa')
        menu=int(input('Sua escolha: '))
        if menu == 1:
            print(f'A soma entre {n1} e {n2} vale {n1+n2}.')
        elif menu == 2:
            print(f'A multiplicação entre {n1} e {n2} resulta em {n1*n2}.')
        elif menu == 3:
            if n1>n2:
                print(f'Entre {n1} e {n2} o maior número é {n1}.')
            elif n1<n2:
                print(f'Entre {n1} e {n2} o maior número é {n2}.')
            else:
                print(f'Entre {n1} e {n2} não existe número maior pois ambos são iguais.')
print('Programa encerrado!')
