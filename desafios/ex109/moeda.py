def moeda (n = 0, moeda = 'R$') :
    return f'{moeda}{n:.2f}'.replace('.',',')


def metade (n, formatado = True) :
    n /= 2
    if formatado :
        return moeda(n)
    return n


def dobro (n, formatado = True) :
    n *= 2
    if formatado :
        return moeda(n)
    return n


def aumentar (n, p, formatado = True) :
    n = n / 100 * (100 + p)
    if formatado :
        return moeda(n)
    return n


def diminuir (n, p, formatado = True) :
    n = n / 100 * (100 - p)
    if formatado :
        return moeda(n)
    return n
