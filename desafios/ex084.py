dados = []
dado = []
maior = menor = 0
while True :
    dado.append ( str ( input ('Nome: ')))
    dado.append ( float ( input ('Peso: ')))
    if len(dados) == 0 :
        maior = menor = dado[1]
    else:
        if dado[1] > maior :
            maior = dado[1]
        elif dado[1] < menor :
            menor = dado[1]
    dados.append (dado[:])
    dado.clear()
    continuar = str ( input ('Quer continuar? '))[0]
    if continuar in 'nN' :
        break
print (f'No total foram cadastradas {len(dados)} pessoas.')
print (f'O maior peso registrado foi {maior:.1f}Kg. peso de:', end='')
for i in dados :
    if i[1] == maior :
        print (f' {i[0]}', end='')
print ('')
print (f'O menor peso registrado foi {menor:.1f}Kg. Peso de:', end='')
for j in dados :
    if j[1] == menor :
        print (f' {j[0]}', end='')
