valores = []
while True :
    valores.append(int ( input ('Digite um número: ')))
    while True:
        continuar = str ( input ('Quer continuar? '))
        if continuar in 'sSnN' :
            break
    if continuar in 'nN' :
        break
valores.sort (reverse=True)
print (f'Foram digitados ao todo {len(valores)} números\nA lista de valores de forma decrescente é {valores}')
if 5 in valores :
    print('E o número 5 foi digitado')
else:
    print('O número 5 não foi digitado')
