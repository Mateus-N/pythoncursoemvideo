from random import choice
a='pedra'
b='papel'
c='tesoura'
lista=[a,b,c]
r=choice(lista)
jogador=str(input('Escolha, Pedra, Papel, Tesoura: ')).lower().strip()
if r == jogador:
    resultado='tivemos um empate!'
else:
    if r == a and jogador == 'papel' or r == b and jogador == 'tesoura' or r == c and jogador == 'pedra':
        resultado='você venceu!!! PARABÉNS!!!'
    else:
        resultado='o computador venceu!!! Mais sorte na próxima!!!'
print(f'O computador escolheu {r} e você escolheu {jogador}, logo {resultado}')
