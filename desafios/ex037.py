num=int(input('Me diga um número: '))
base=int(input('Você quer converter ele para: \n [ 1 ] Bínario \n [ 2 ] Octal \n [ 3 ] Hexadecimal \n Sua opção: '))
if base == 1:
    print(f'O número {num} quando convertido para bínario vale {bin(num)[2:]}!')
elif base == 2:
    print(f'O número {num} quando convertido para octal vale {oct(num)[2:]}!')
elif base == 3:
    print(f'O número {num} quando convertido para hexadecimal vale {hex(num)[2:]}!')
else:
    print('Opção inválidade. Tente novamente')
