m=0
mv=''
ih=0
im=0
for x in range(1,5):
    print(f'\033[1m------ {x}ª PESSOA -----\033[m')
    nome=str(input(f'Nome? ')).strip()
    idade=int(input('Idade? '))
    sexo=str(input('Sexo [M/F]: '))
    if x == 1:
        ih=idade
    if sexo in 'Mm' and idade >= ih:
        mv=str(nome)
    elif sexo in 'Ff' and idade<21:
        im+=1
    m+=idade
print(f'A média de idade do grupo é {m/4} anos')
if mv == 'nome':
    print('Não há homens no grupo')
else:
    print(f'O homem mais velho do grupo se chama {mv}')
if im == 0:
    print('Não há mulheres no grupo')
else:
    print(f'No grupo temos {im} mulheres com menos de 21 anos')
