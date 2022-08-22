num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort (reverse=True)
num.insert (2, 2)
num.pop(1)
if 4 in num :
    num.remove(4)
else:
    print ('Não achei o valor 4')
print (num)
print (f'Essa lista tem {len(num)} valores')
