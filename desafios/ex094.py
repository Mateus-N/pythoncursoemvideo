pessoas = {}
bancodedados = []
idademaiorquemédia = []
idadetotal = 0
while True :
    pessoas['nome'] = str ( input ('Nome: '))
    while True :
        pessoas['sexo'] = str ( input ('Sexo [M/F]: '))[0]
        if pessoas['sexo'] in 'mMfF' :
            break
        print ('Opção inválida! Digite apenas M ou F.')
    pessoas['idade'] = int ( input ('Idade: '))
    idadetotal += pessoas['idade']
    bancodedados.append (pessoas.copy())
    while True :
        continuar = str ( input ('Quer continuar [S/N]? '))[0]
        if continuar in 'nNsS' :
            break
        print ('Opção inválida! Digite apenas S ou N.')
    if continuar in 'nN' :
        break
média = idadetotal / len(bancodedados)
print (f'A -) Ao todo foram cadastradas {len(bancodedados)} pessoas.')
print (f'B -) A média de idade do grupo é de {média:5.2f} anos')
print ('C -) As mulheres cadastradas foram:', end='')
for i in bancodedados :
    if i['sexo'] in 'fF' :
        print (f' {i["nome"]}', end='')
print('')
print ('D -) As pessoas com idade acima da média foram:')
for i in bancodedados :
    if i['idade'] > média :
        for k, v in i.items() :
            print (f'   => {k} = {v}; ',end='')
        print ('')
print ('<< ENCERRADO! >>')
