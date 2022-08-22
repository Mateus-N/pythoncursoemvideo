soma = contador = 0
while True:
    num = int ( input ('Digite um número (999 para parar): '))
    if num == 999:
        break
    soma += num
    contador += 1
print (f'Foram digitados {contador} números e a soma entre eles vale {soma}!')
