valores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
indice = [11, 5, 1, 9, 12]
correspondente = []
for c in indice :
    if c <= len(valores) :
        valor = c
    else:
        valor = 'none'
    correspondente.append (valor)
print (correspondente)
