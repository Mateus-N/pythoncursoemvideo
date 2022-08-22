notascinquenta = notasvinte = notasdez = notasum = valorvinte = valordez = 0
valor = int (input ('Que valor você quer sacar? R$'))
notascinquenta = valor // 50
valorvinte = valor % 50
notasvinte = valorvinte // 20
valordez = valorvinte % 20
notasdez = valordez // 10
notasum = valordez % 10
if notascinquenta > 0 :
    print (f'Total de {notascinquenta} cédulas de R$50')
if notasvinte > 0 :
    print (f'Total de {notasvinte} cédulas de R$20')
if notasdez > 0 :
    print (f'Todas de {notasdez} cédulas de R$10')
if notasum > 0 :
    print (f'Totas de {notasum} cédulas de R$1')
print ('Volte sempre! Tenha um bom dia!')
