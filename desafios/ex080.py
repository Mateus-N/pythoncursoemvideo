valores = []
for i in range (0,5) :
    numero = int ( input ('Digite um número: '))
    if i == 0 or numero >= max (valores) :
        valores.append(numero)
    elif numero <= min (valores) :
        valores.insert (0, numero)
    else :
        if len(valores) == 2 :
            valores.insert (1,numero)
        elif len(valores) == 3 :
            if numero <= valores[1] :
                valores.insert (1,numero)
            else :
                valores.insert (2,numero)
        elif len(valores) == 4 :
            if numero <= valores[1] :
                valores.insert (1,numero)
            elif numero >= valores[2] :
                valores.insert (3,numero)
            else:
                valores.insert (2,numero)
print(f'Os valores digitados e em ordem foram: {valores}')
