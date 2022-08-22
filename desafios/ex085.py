valores = [[], []]
for c in range (0, 7) :
    numero = int ( input (f'Digite o {c+1}° valor: '))
    if numero % 2 == 0 :
        valores[0].append (numero)
    else:
        valores[1].append (numero)
valores[0].sort()
valores[1].sort()
print (f'''Os valores pares digitados foram {valores[0]}
Os valores ímpares digitados foram {valores[1]}''')
