maiores = quantidadehomens = quantidademulheres = 0
while True :
    idade = int ( input ('Idade: '))
    while True :
        sexo = str ( input ('Sexo [M/F]: '))[0]
        if sexo in 'mMfF':
            break
    if idade >= 18 :
        maiores += 1
    if sexo in 'mM' :
        quantidadehomens += 1
    if sexo in 'fF' and idade < 20:
        quantidademulheres += 1
    while True :
        continuar = str ( input ('Quer continuar [S/N] ? '))[0]
        if continuar in 'sSnN':
            break
    if continuar in 'nN' :
        break
print (f'No total foram {maiores} pessoas maiores de 18 anos.\nTivemos {quantidadehomens} homens cadastrados.\nE {quantidademulheres} mulheres com menos de 20 anos.')
