def contador (*num) :
    for valor in num :
        print (valor, end=' ')
    print ('')
    tam = len (num)
    print (f'Recebi os valores {num} e são ao todo {tam} números')
    
contador (2, 1, 7)
contador (8, 0)
contador (4, 4, 7, 6, 2)
