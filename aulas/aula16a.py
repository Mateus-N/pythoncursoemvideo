lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
print (lanche[-2:])
print ( len (lanche))

for comer in lanche :
    print (comer)

for pos, comida in enumerate(lanche) :
    print (f'{comida} na posição {pos}')

for cont in range ( 0 , len (lanche)):
    print (lanche[cont], f'posição {cont}')

print ( sorted (lanche))