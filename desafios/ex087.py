matriz = [[], [], []]
somapares = somaterceiracoluna = maiorsegundalinha = 0
for i in range (0, 3) :
    for j in range (0, 3) :
        matriz[i].append ( int ( input (f'Digite um valor para [{i}, {j}] : ')))
for i in range (0, 3) :
    for j in range (0, 3) :
        print (f'[ {matriz[i][j]} ]', end='')
        if matriz[i][j] % 2 == 0 :
            somapares += j
    print ('')
print (f'A soma de todos os valores pares digitados é {somapares}')
for i in range (0, 3) :
    somaterceiracoluna += matriz[i][2]
print (f'A soma de todos os valores da terceira coluna é {somaterceiracoluna}')
for i in range (0, 3) :
    if matriz[1][i] > maiorsegundalinha :
        maiorsegundalinha = matriz[1][i]
print (f'O maior valor da segunda linha é {maiorsegundalinha}')
