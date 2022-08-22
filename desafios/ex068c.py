from random import randint
vitoria = 0
while True :
    numerocomputador = randint(0,10)
    numerojogador = int ( input ('Diga um valor: '))
    while True :
        tipo = str ( input ('Par ou ímpar [P/I] ? '))
        if tipo in 'pPiI' :
            break
    soma = numerocomputador + numerojogador
    print (f'Você jogou {numerojogador} e o computador {numerocomputador}. Total de {soma}', end='')
    print ('DEU PAR' if soma % 2 == 0 else 'DEU ÍMPAR')
    if tipo in 'pP' :
        if soma % 2 == 0 :
            print ('Você VENCEU!')
        else:
            print ('Você PERDEU!')
            break
    elif tipo in 'iI' :
        if soma % 2 == 1 :
            print ('Você VENCEU!')
        else:
            print ('Você PERDEU!')
            break
    vitoria += 1
    print ('Vamos jogar novamente!')
print (f'GAME OVER! Você venceu {vitoria} vezes!')
