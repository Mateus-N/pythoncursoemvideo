soma = contador = maior = menor = 0
continuar = 'S'
while continuar in 'Ss' :
    numero = int ( input ('Digite um número: '))
    contador += 1
    soma += numero
    if contador == 1 :
        maior = menor = numero
    else:
        if numero > maior :
            maior = numero
        elif numero < menor :
            menor = numero
    continuar = str ( input ('Quer continuar a digitar valores [S/N]? '))
media = soma / contador
print (f'A média entre todos os valores é {media:.2f}. \nO maior valor entre todos digitados é {maior}. \nO menor valor entre todos digitados é {menor}.')
