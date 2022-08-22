from random import randint
contador = 0
while True :
    numerocomputador = randint(0,10)
    numerojogador = int ( input ('Diga um valor: '))
    tipo = str ( input ('Par ou ímpar [P/I] ? '))
    soma = numerocomputador + numerojogador
    if tipo not in 'pPiI' :
        print ('Valor inválido!')
    elif soma % 2 == 0 :
        if tipo in 'Pp' :
            print (f'Sua escolha foi {numerojogador} e o computador escolheu {numerocomputador}, a soma entre eles vale {soma} que é PAR, logo, você venceu!')
        elif tipo in 'Ii' :
            print (f'Sua escolha foi {numerojogador} e o computador escolheu {numerocomputador}, a soma entre eles vale {soma} que é PAR, logo, você perdeu!')
            break
    elif soma % 2 == 1 :
        if tipo in 'Ii' :
            print (f'Sua escolha foi {numerojogador} e o computador escolheu {numerocomputador}, a soma entre eles vale {soma} que é ÍMPAR, logo, você venceu!')
        elif tipo in 'Pp' :
            print (f'Sua escolha foi {numerojogador} e o computador escolheu {numerocomputador}, a soma entre eles vale {soma} que é ÍMPAR, logo, você perdeu!')
            break
    print ('Vamos jogar novamente!')
    contador += 1
print (f'GAME OVER! Você venceu {contador} vezes.')
