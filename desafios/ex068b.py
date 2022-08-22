from random import randint
numerocomputador = randint(0,10)
contador = 0
while True :
    numerojogador = int ( input ('Diga um valor: '))
    escolhajogador = str ( input ('Par ou ímpar [P/I] ? '))
    soma = numerocomputador + numerojogador
    parouimpar = ''
    resultado = ''
    if soma % 2 == 0 :
        parouimpar = 'PAR'
    else:
        parouimpar = 'ÍMPAR'
    if escolhajogador not in 'pPiI' :
        print ('Valor inválido!')
    else:
        if soma % 2 == 0 :
            if escolhajogador in 'Pp' :
                resultado = 'VENCEU!'
            elif escolhajogador in 'Ii' :
                resultado = 'PERDEU!'
        elif soma % 2 == 1 :
            if escolhajogador in 'Ii' :
                resultado = 'VENCEU!'
            elif escolhajogador in 'Pp' :
                resultado = 'PERDEU!'
        print (f'Você jogou {numerojogador} e o computador jogou {numerocomputador}. Total de {soma} que é {parouimpar}\nVocê {resultado}')
        if resultado == 'PERDEU!' :
            break
        contador += 1
    print ('Vamos jogar novamente!')
print (f'GAME OVER! Você venceu {contador} vezes.')
