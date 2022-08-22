from math import radians,sin,cos,tan
an=float(input('Digite um ângulo e lhe direi o seno, o cosseno e a tangente: '))
n=radians(an)
s=sin(n)
c=cos(n)
t=tan(n)
print('Referente ao ângulo {:.1f}°, o seno é {:.2f}, o cosseno {:.2f} e a tangente é {:.2f}.'.format(an,s,c,t))
