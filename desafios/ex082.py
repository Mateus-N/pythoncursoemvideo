valores = []
pares = []
ímpares = []
while True :
    valores.append(int ( input ('Digite um número: ')))
    while True:
        continuar = str ( input ('Quer continuar? '))
        if continuar in 'sSnN' :
            break
    if continuar in 'nN' :
        break
for i in valores :
    if i % 2 == 0 :
        pares.append(i)
    else:
        ímpares.append(i)
valores.sort()
pares.sort()
ímpares.sort()
print (f'''A lista de valores digitados é: {valores}
A lista contendo apenas valores pares é: {pares}
A lista contendo apenas valores ímpares é: {ímpares}''')
