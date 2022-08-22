parentesesaberto = []
parentesesfechado = []
expressão = str ( input ('Digite sua expressão: '))
for i in expressão :
    if i == '(' :
        parentesesaberto.append(i)
    elif i == ')' :
        parentesesfechado.append(i)
if len(parentesesaberto) == len(parentesesfechado) :
    print ('Sua expressão está correta!')
else:
    print ('Sua expressão está errada!')
