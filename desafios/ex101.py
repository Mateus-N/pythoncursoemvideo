def voto (ano) :
    from datetime import date
    idade = date.today().year - ano
    if 65 > idade >= 18 :
        return f'Com {idade} anos: VOTO OBRIGATÓRIO!'
    elif idade >= 16 or idade >= 65 :
        return f'Com {idade} anos: VOTO OPCIONAL.'
    else:
        return f'Com {idade} anos: NÃO VOTA'


nascimento = int ( input ('Em que ano você nasceu? '))
print (voto (nascimento))
