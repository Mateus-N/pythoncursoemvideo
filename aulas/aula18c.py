galera = []
dados = []
totalmaior = totalmenor = 0
for i in range (0, 5) :
    dados.append ( str ( input ('Nome: ')))
    dados.append ( int ( input ('idade: ')))
    galera.append (dados[:])
    dados.clear()
print (galera)
for j in galera :
    if j[1] >= 21 :
        print (f'{j[0]} é maior de idade.')
        totalmaior += 1
    else:
        print (f'{j[0]} é menor de idade.')
        totalmenor += 1
print (f'Temos {totalmaior} maiores de idade e {totalmenor} menores de idade.')
