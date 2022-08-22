valores = []
while True :
    numero = int ( input ('Digite um número: '))
    if numero not in valores :
        valores.append (numero)
        print ('Número adicionado na lista!')
    else:
        print ('Valor repetido e não será adicionado!')
    while True:
        continuar = str ( input ('Quer continuar? '))
        if continuar in 'sSnN' :
            break
    if continuar in 'nN' :
        break
valores.sort()
print (f'Todos os valores unicos digitados foram: {valores}')
