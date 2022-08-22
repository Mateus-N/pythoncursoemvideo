from random import randint
from time import sleep
palpites = []
tentativas = int ( input ('Quantos jogos você preetende fazer? '))
for i in range (0, tentativas) :
    palpites.append([])
    while not len(palpites[i]) == 6 :
        numero = randint(1, 60)
        if numero not in palpites[i] :
            palpites[i].append(numero)
    palpites[i].sort()
    sleep(1)
    print (f'Jogo {i+1}: {palpites[i]}')
