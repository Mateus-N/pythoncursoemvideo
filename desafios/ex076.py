contador = 0
tupla = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.9, 'Estojo', 25, 'Transferidor', 4.2, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.3, 'Livro', 34.9)
for i in tupla :
    contador += 1
    if contador % 2 == 1 :
        print (f'{i:.<30}', end=' ')
    else:
        print (f'R${i:>7.2f}')
