from datetime import date
s=0
for c in range(1,8):
    ano=int(input(f'Em que ano a {c}ª pessoa nasceu? '))
    if ano+21<=date.today().year:
        s+=1
n=7-s
print(f'No total {n} pessoas são menores de idade \nE também tivemos {s} pessoas maiores de idade')
