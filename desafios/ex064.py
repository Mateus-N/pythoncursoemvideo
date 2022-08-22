numero = contador = soma = 0
numero = int ( input ('Digite um número inteiro [999 para parar]: '))
while numero != 999 :
    contador += 1
    soma += numero
    numero = int ( input ('Digite um número inteiro [999 para parar]: '))
print (f'A quantidade de números digitados foi de {contador} e soma total entre eles vale {soma}.')
