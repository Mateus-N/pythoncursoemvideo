numeros = ( int ( input ('Digite um número: ')), int ( input ('Digite outro número: ')), int ( input ('Digite outro número: ')), int ( input ('Digite outro número: ')))
print (f'Você digitou os valores: {numeros}')
print (f'O valor 9 apareceu {numeros.count(9)} vezes')
temtres = int (numeros.count(3))
if temtres == 0 :
    print ('O valor 3 não foi digitado em nenhuma posição')
else:
    tres = int (numeros.index(3))
    print (f'O valor 3 foi digitado na {tres+1}ª posição')
print ('Os valores pares digitados foram: ', end='')
for j in numeros :
    if j % 2 == 0 :
        print(j, end=' ')
