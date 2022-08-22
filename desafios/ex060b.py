n=int(input('Digite um valor: '))
r=1
for i in range(n,0,-1):
    r*=i
print(f'O fatorial de {n} ou {n}! é {r}')
