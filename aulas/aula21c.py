def fatorial (numero = 1) :
    f = 1
    for c in range (numero, 0, -1) :
        f *= c
    return f


n = int ( input ('Digite um número: '))
print (f'O fatorial de {n} é igual a {fatorial(n)}')

def fatorial (n) :
    f = 1
    i = 2
    while i <= n :
        f *= i
        i += 1
    return f


print ( fatorial(5))
