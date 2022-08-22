from random import randint
num=int(randint(0,5))
print('Pensei em um número de 0 a 5. Tente advinhar...')
user=int(input('Se arrisca em acertar qual foi? '))
if user == num:
    print('Parabéns, você acertou!')
else:
    print('Você errou, o número era {}, mais sorte na próxima!'.format(num))
