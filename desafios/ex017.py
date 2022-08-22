from math import hypot
co=float(input('Digite o comprimento do cateto oposto da hipotenusa: '))
ca=float(input('Digite o comprimento do cateto adjacente da hipotenusa: '))
h=hypot(co,ca)
print('Se um triângulo retângulo tem o cateto oposto medindo {:.2f} e o cateto adjacente medindo {:.2f}, sua hipotenusa mede {:.2f}'.format(co,ca,h))
