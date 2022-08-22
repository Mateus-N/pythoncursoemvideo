def teste () :
    global n1
    n1 = 4
    x = 8
    print (f'Na função teste, x vale {x}')
    print (f'Na função teste, n1 vale {n1}')
# x é uma variavél local
# n é uma variavél global

n1 = 2
teste ()
print (f'No programa principal, n1 vale {n1}')
