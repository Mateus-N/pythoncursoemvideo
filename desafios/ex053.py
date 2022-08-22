f=str(input('Digite uma frase: ')).upper().strip().split()
f1=''.join(f)
f2=f1[::-1]
print(f'O contrário de {f1} é {f2}')
if f1==f2:
    print('SIM, essa frase é um palíndromo!')
else:
    print('NÃO é um palíndromo, tente outra frase por favor.')
