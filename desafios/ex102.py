def fatorial (numero, show = False) :
    """
    -> calcula o fatorial de um número.
    :parametro numero: O número a ser calculado.
    :parametro show: (opcional) Mostra ou não a conta
    :return: O valor do Fatorial do número numero.
    """
    f = 1
    for c in range (numero, 0, -1) :
        if show:
            if c > 1 :
                print (f'{c} x ', end='')
            else :
                print (f'{c} = ', end='')
        f *= c
    return f


n = int ( input ('Digite um número: '))
show = str ( input ('Quer ver o cálculo? '))[0]
if show in 'sS' :
    show = True
else:
    show = False
print ( fatorial (n, show))
