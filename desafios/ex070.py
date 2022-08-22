totalgasto = contadormaisdemil = menorpreço = contador = 0
while True :
    nomedoproduto = str ( input ('Nome do produto: '))
    preço = float ( input ('Preço do produto: R$'))
    totalgasto += preço
    contador += 1
    if preço > 1000 :
        contadormaisdemil += 1
    if contador == 1 or preço < menorpreço :
        menorpreço = preço
        nomemaisbarato = nomedoproduto
    while True :
        continuar = str ( input ('Quer continuar [S/N]?'))[0]
        if continuar in 'nNsS' :
            break
    if continuar in 'nN' :
        break
print (f'O preço total dos produtos é R${totalgasto:.2f}!\nAo final tivemos {contadormaisdemil} produtos acima dos R$1000\nO produto mais barato foi {nomemaisbarato} no valor de R${menorpreço:.2f}')
