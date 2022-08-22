while True:
    número = int ( input ('Digite um número e lhe mostrarei sua tabuada: '))
    if número < 0:
        break
    for c in range(1,11):
        print(f'{número} x {c:2} = {número*c}')
print ('FIM')
