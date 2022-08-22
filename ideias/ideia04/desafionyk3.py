def f(n) :
    if n < 2 :
        return 1
    return f(n - 1) * n


numero = int ( input ('Digite um valor para ter seu fatorial > '))
print ( f(numero))
