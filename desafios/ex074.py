from random import randint
contador = maior = menor = 0
numeros = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))
print ('Os valores sorteados foram: ', end='')
for i in numeros :
    print(i, end=' ')
    contador += 1
    if contador == 1 :
        maior = i
        menor = i
    else:
        if i > maior :
            maior = i
        elif i < menor :
            menor = i
print ('')
print (f'O maior valor sorteado foi {maior}\nO menor valor sorteado foi {menor}')
