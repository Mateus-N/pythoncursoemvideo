from time import sleep
def maior (*valores) :
    max = 0
    print ('-='*45)
    print (f'Analisando os valores passados...')
    sleep (1)
    for c, i in enumerate(valores) :
        print (i, end=' ')
        if c == 0 or i > max :
            max = i
    print (f'   => Foram informados ao todo {len(valores)} valores')
    print (f'O maior valor informado foi {max}')


maior (2, 9, 4, 5, 6, 3)
maior (1, 6, 0, 3)
maior (4, 3, 0, 2, 3)
maior ()
maior (2)
