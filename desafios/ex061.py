t1=float(input('Qual o primeiro termo da PA: '))
r=float(input('Qual a razão da PA: '))
tn=0
i=0
while i<=9:
    i+=1
    tn=t1+(i-1)*r
    print(f'O {i}° termo da PA é {tn:.1f}!')
