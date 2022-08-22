from random import randint
from time import sleep
itens=('Pedra','Papel','Tesoura','Spock','Lagarto')
computador=randint(0,4)
print('Suas opções: \n [ 0 ] Pedra \n [ 1 ] Papel \n [ 2 ] Tesoura \n [ 3 ] Spock \n [ 4 ] Lagarto')
jogador=int(input('Qual sua jogada? '))
print('-='*15)
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO!')
sleep(0.5)
print('-='*15)
print(f'O computador jogou {itens[computador]}')
print(f'Você jogou {itens[jogador]}')
print('-='*15)
if computador == jogador:
    print('EMPATE!')
elif computador != jogador:
    if computador == 0: #pedra
        if jogador == 1: #papel
            print('Papel cobre pedra. VOCÊ GANHOU!')
        elif jogador == 2: #tesoura
            print('Pedra destrói tesoura. VOCÊ PERDEU!')
        elif jogador == 3: #spock
            print('Spock vaporiza pedra. VOCÊ GANHOU!')
        elif jogador == 4: #lagarto
            print('Pedra esmaga lagarto. VOCÊ PERDEU!')
        else:
            print('Jogada inválida')
    elif computador == 1: #papel
        if jogador == 0: #pedra
            print('Papel cobre pedra. VOCÊ PERDEU!')
        elif jogador == 2: #tesoura
            print('Tesoura corta papel. VOCÊ GANHOU!')
        elif jogador == 3: #spock
            print('Papel desaprova o Spock. VOCÊ PERDEU!')
        elif jogador == 4: #lagarto
            print('Lagarto come papel. VOCÊ GANHOU!')
        else:
            print('Jogada inválida')
    elif computador == 2: #tesoura
        if jogador == 0: #pedra
            print('Pedra destrói tesoura. VOCÊ GANHOU!')
        elif jogador == 1: #papel
            print('Tesoura corta papel. VOCÊ PERDEU!')
        elif jogador == 3: #spock
            print('Spock quebra a tesoura. VOCÊ GANHOU!')
        elif jogador == 4: #lagarto
            print('Tesoura decapita o lagarto. VOCÊ PERDEU!')
        else:
            print('Jogada inválida')
    elif computador == 3: #spock
        if jogador == 0: #pedra
            print('Spock vaporiza a pedra. VOCÊ PERDEU!')
        elif jogador == 1: #papel
            print('Papel desaprova o Spock. VOCÊ GANHOU')
        elif jogador == 2: #tesoura
            print('Spock quebra a tesoura. VOCÊ PERDEU!')
        elif jogador == 4: #lagarto
            print('Lagarto envenena o Spock. VOCÊ GANHOU!')
        else:
            print('Jogada inválida')
    elif computador == 4: #lagarto
        if jogador == 0: #pedra
            print('Pedra esmaga lagarto. VOCÊ GANHOU!')
        elif jogador == 1: #papel
            print('Lagarto come papel. VOCÊ PERDEU!')
        elif jogador == 2: #tesoura
            print('Tesoura decapita lagarto. VOCÊ GANHOU!')
        elif jogador == 3: #spock
            print('Lagarto evenena o Spock. VOCÊ PERDEU!')
        else:
            print('Jogada inválida')
else:
    print('Jogada inválida')
print('-='*15)