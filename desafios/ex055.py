max=0
min=0
for c in range(1,6):
    peso=float(input(f'Peso da {c}ª pessoa: '))
    if c == 1:
        max=peso
        min=peso
    else:
        if peso>=max:
            max=peso
        elif peso<=min:
            min=peso
print(f'O maior peso lido é: {max}Kg \nO menor peso lido é {min}Kg')
