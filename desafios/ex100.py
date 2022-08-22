from random import randint

def sorteia (lista) :
    print ('Sorteando os 5 valores da lista: ', end='')
    for i in range (0, 5) :
        num = (randint(0, 10))
        print (num, end=' ')
        lista.append (num)
    print ('PRONTO!')

def somapar (lista) :
    soma = 0
    for i in lista :
        if i % 2 == 0 :
            soma += i
    print (f'Somando os valores pares de {numeros}, temos {soma}')


numeros = []
sorteia (numeros)
somapar (numeros)
