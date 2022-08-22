num=float(input('Qual a distância da viagem? '))
if num <= 200:
    p=num*0.5
else:
    p=num*0.45
print('Para uma viagem de {:.2f}Km o valor da sua passagem será R${:.2f}'.format(num,p))
