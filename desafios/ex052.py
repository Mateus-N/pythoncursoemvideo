n=int(input('Digite um número inteiro: '))
resultado='não é'
s=0
for c in range(2,n):
    if n%c==0:
        s+=1
if s == 0:
    resultado='é'
print(f'O número {n} {resultado} um número primo pois ele é divisivel apenas por 1 e por ele mesmo!')
