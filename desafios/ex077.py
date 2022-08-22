tupla = ('Mateus', 'Adrielly', 'Castiel', 'Estudo', 'Notebook', 'Celular', 'Mouse', 'Controle', 'Jogo', 'Tela')
for i in tupla :
    print(f'Na palavra {i} temos as vogais', end='')
    for j in i :
        if j in 'aAeEiIoOuU' :
            print (f' {j}', end='')
    print ('')
