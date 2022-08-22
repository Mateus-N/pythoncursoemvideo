from random import randint
num=randint(1,100)
print('O computador escolheu aleátoriamente um número de 1 a 100. Tente advinhar, você tem 6 tentativas!')
for x in range(1,7):
    jogador=int(input(f'{x}ª Tentativa: '))
    if jogador == num:
        print(f'PARABÉNS. Você acertou! \n O número era {num}!')
        break
    elif x == 6 and jogador != num:
        print(f'Sinto muito, você PERDEU! o número escolhido era {num}')
    else: 
        if jogador > num:
            print(f'O número escolhido é MENOR que {jogador}')
        elif jogador < num:
            print(f'O número escolhido é MAIOR que {jogador}')
        if x == 3:
            dica=str(input('Quer uma dica [S/N]? '))
            if dica in 'Ss':
                if num%2 == 0:
                    print('O número escolhido pelo computador é PAR!')
                else:
                    print('O número escolhido pelo computador é ÍMPAR!')
