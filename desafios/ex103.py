def ficha (nome, gols) :
    """
    Mostra os dados passados na tela
    :parametro nome: nome do jogador
    :parametro gols: quantidade de gols feitos no campeonato
    """
    if nome == '' :
        nome = '<desconhecido>'
    if gols == '' :
        gols = 0
    else:
        if gols.isnumeric() :
            gols = int (gols)
        else: gols = 0
    return f'O jogador {nome} fez {gols} gol(s) no campeonato.'


nome = str ( input ('Nome do jogador: '))
gols = str ( input ('Número de Gols: '))
print ( ficha (nome, gols))
help (ficha)
