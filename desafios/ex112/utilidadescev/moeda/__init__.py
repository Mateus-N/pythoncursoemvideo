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


def linha (tam) :
    print ('-'*tam)


def titulo (texto) :
    linha (30)
    print (f'{texto:^30}')
    linha (30)


def resumo(n = 0, a = 10, d = 10) :
    titulo ('RESUMO DO VALOR')
    print(f'Preço analisado: \t{moeda(n)}')
    print(f'Dobro do preço: \t{dobro(n)}')
    print(f'Metade do preço: \t{metade(n)}')
    print(f'{a}% de aumento: \t{aumentar(n, a)}')
    print(f'{d}% de redução: \t{diminuir(n, d)}')
    linha(36)
