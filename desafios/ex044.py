preco=float(input('Qual o preço normal do produto? '))
print('Qual a forma de pagamento? \n 1 - Dinheiro \n 2 - PIX \n 3 - Cheque \n 4 - Débito \n 5 - Crédito')
pag=str(input('Forma de pagamento: '))
if pag == '1' or pag == '2' or pag == '3':
    preco=preco/100*90
elif pag == '4':
    preco=preco/100*95
elif pag == '5':
    print('Parcelamento: \n 1 - A vista \n 2 vezes \n 3 vezes \n 4 vezes \n 5 vezes \n 6 vezes')
    parcelas=int(input('Em quantas vezes? '))
    if parcelas == 2:
        preco=preco/100*105
    elif parcelas == 3 or parcelas == 4 or parcelas == 5 or parcelas == 6:
        preco=preco/100*115
print('Com esse meio de pagamento o preço final do produto fica de R${:.2f}!'.format(preco))
if pag == '5':
    print('E fica em {} parcela(s) no valor R${:.2f}'.format(parcelas,preco/parcelas))
