n1=float(input('Primeira nota: '))
n2=float(input('Segunda nota: '))
m=(n1+n2)/2
if m<5:
    print(f'REPROVADO! A sua média foi apenas {m:.1f}.')
elif 5<=m<=6.9:
    print(f'RECUPERAÇÃO! A sua média foi de {m:.1f}.')
else:
    print(f'APROVADO! A sua média foi de {m:.1f}, parabéns!')
