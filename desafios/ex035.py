a=float(input('Primeiro segmento: '))
b=float(input('Segundo segmento: '))
c=float(input('Terceiro segmento: '))
tri=('não pode')
if a+b>c and b+c>a and a+c>b:
    tri=('pode')
print(f'A junção destes três segmentos {tri} formar um triâgulo')
