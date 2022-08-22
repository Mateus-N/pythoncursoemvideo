valores = []
valores.append(5)
valores.append(9)
valores.append(4)
for valor in valores :
    print (valor, end=' ')
print ('')
for c, valor in enumerate(valores) :
    print(f'Na posição {c} encontrei o valor {valor}!')
