def soma (*num) :
    s = 0
    for i in num:
        s += i
    print (f'Somando os valores {num} temos {s}.')

soma (4, 5)
soma (8, 9, 5)
soma (2, 1, 4, 6)
