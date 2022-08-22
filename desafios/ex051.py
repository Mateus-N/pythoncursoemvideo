t1=float(input('Qual o primeiro termo da PA: '))
r=float(input('Qual a razão da PA: '))
tn=0
for c in range(1,11):
    tn=t1+(c-1)*r
    print(f'O {c}° termo da PA é {tn:.1f}!')
