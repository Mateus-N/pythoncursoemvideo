time = []
jogador = {}
golsporpartida = []
while True :
    jogador['nome'] = str ( input ('Nome do jogador: '))
    partidas = int ( input (f'Quantas partidas {jogador["nome"]} jogou? '))
    totaldegols = 0
    for i in range (0, partidas) :
        gols = int ( input (f'Quantos gols na partida {i+1}? '))
        golsporpartida.append (gols)
        totaldegols += gols
    jogador['gols'] = golsporpartida[:]
    jogador['total'] = totaldegols
    time.append (jogador.copy())
    jogador.clear()
    golsporpartida.clear()
    while True :
        continuar = str ( input ('Quer continuar? '))[0]
        if continuar in 'nNsS' :
            break
        print ('Opção inválida! Digite apenas S ou N.')
    if continuar in 'nN' :
        break
    print ('-'*30)
print ('-='*50)
print (f'{"cod.":<5} {"Nome":<15} {"Gols":<20} Total')
print ('-'*60)
for c, i in enumerate(time) :
    print (f'{c:<5} {i["nome"]:<15} {i["gols"]!s:<20s} {i["total"]}')
print ('-'*60)
while True :
    dados = int ( input ('Mostrar dados de qual jogador? '))
    print ('-'*60)
    if dados == 999 :
        print ('-'*60)
        break
    elif dados < 0 or dados > len(time) :
        print (f'Não existe jogador com código {dados}! Tente novamente')
    else:
        print (f'Levantamento do jogador {time[dados]["nome"]}:')
        for i in range (0, len(time[dados]['gols'])) :
            print (f'No jogo {i+1} ele fez {time[dados]["gols"][i]} gols.')
print ('<<< VOLTE SEMPRE!!! >>>')
