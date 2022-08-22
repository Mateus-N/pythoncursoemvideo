from cmath import sqrt
from random import randint, random
import emoji
num=int(input('Digite um número: '))
raiz=sqrt(num)
print('A raiz de {} é igual a {:.2f}'.format(num,raiz))

num=randint(1,100)
print('{}'.format(num))

print(emoji.emojize('Python é 🌎'))