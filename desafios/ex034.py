sal=float(input('Qual seu salário atual? '))
maior=sal/100*110
menor=sal/100*115
if sal > 1250.00:
    print('Seu salário atual é de {:.2f} e terá um aumento de 10%, seu novo salário após o aumento será de {:.2f}'.format(sal,maior))
else:
    print('Seu salário atual é de {:.2f} e terá um aumento de 15%, seu novo salário após o aumento será de {:.2f}'.format(sal,menor))
