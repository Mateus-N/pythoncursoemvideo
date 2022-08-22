valor = int (input ('Que valor você quer sacar? R$'))
cedulas = 50
totalcedulas = 0
while True :
    if valor >= cedulas:
        valor -= cedulas
        totalcedulas += 1
    else:
        print (f'Total de {totalcedulas} cédulas de R${cedulas}')
        if cedulas == 50 :
            cedulas = 20
        elif cedulas == 20 :
            cedulas = 10
        elif cedulas == 10 :
            cedulas = 1
        totalcedulas = 0
        if valor == 0:
            break
