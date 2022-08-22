n=''
par=impar=0
while n!=0:
    n=int(input('Digite uma valor: '))
    if n==0:
        break
    if n%2 == 0:
        par+=1
    else:
        impar+=1
print(f'No total foram {par} números pares e {impar} números ímpares.')
