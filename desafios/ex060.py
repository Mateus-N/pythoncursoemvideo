num = int ( input ('Digite um valor: '))
i = num
r = 1
while i > 0:
    print(f'{i}', end='')
    print(' x ' if i > 1 else ' = ', end='')
    r *= i
    i -= 1
print (r)
print (f'O fatorial de {num} ou {num}! é {r}')
