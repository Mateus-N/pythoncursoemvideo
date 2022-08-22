jogador = {}
golsporpartida = []
totaldegols = 0
jogador['nome'] = str ( input ('Nome do jogador: '))
partidas = int ( input (f'Quantas partidas {jogador["nome"]} jogou? '))
for i in range (0, partidas) :
    gols = int ( input (f'Quantos gols na partida {i+1}? '))
    golsporpartida.append (gols)
    totaldegols += gols
jogador['gols'] = golsporpartida[:]
jogador['total'] = totaldegols
print ('-='*40)
print (jogador)
print ('-='*40)
for k, v in jogador.items() :
    print (f'O campo {k} tem o valor {v}.')
print ('-='*40)
print (f'O jogador {jogador["nome"]} jogou {partidas} partidas.')
for i in range (0, partidas) :
    print (f'   => Na partida {i+1}, fez {jogador["gols"][i]} gols.')
print (f'Fez um total de {totaldegols} gols')
