valores = []
max = min = 0
for i in range (0,5) :
    valores.append ( int ( input (f'Digite um valor na posição {i}: ')))
    if i == 0 :
        max = min = valores[i]
    else:
        if valores[i] > max :
            max = valores[i]
        elif valores[i] < min :
            min = valores[i]
print (f'Você digitou os valores {valores}')
print (f'O maior valor digitado foi {max} nas posições: ', end='')
for j, v in enumerate(valores) :
    if v == max :
        print (f'{j}...', end='')
print ('')
print (f'O menor valor digitado foi {min} nas posições: ', end='')
for i, v in enumerate(valores) :
    if v == min :
        print (f'{i}...', end='')
print ('')
