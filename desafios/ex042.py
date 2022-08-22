a=float(input('Primeiro segmento: '))
b=float(input('Segundo segmento: '))
c=float(input('Terceiro segmento: '))
tri=('não pode')
if a+b>c and a+c>b and b+c>a:
    tri=('pode')
    tipo=('Escaleno')
    if a==b==c:
        tipo=('Equilátero')
    elif a==b or a==c or b==c:
        tipo=('Isósceles')
print(f'A junção destes três segmentos {tri} formar um triângulo!')
if tri == 'pode':
    print(f'O triângulo formado será do tipo {tipo}')
