from datetime import date
ano=int(input('Digite um ano e lhe direi se ele é um ano bissexto. Coloque 0 para o ano atual: '))
if ano == 0:
    ano=date.today().year
if ano%4 == 0 and ano%100 != 0 or ano%400 == 0:
    print('O ano de {} é um ano bissexto!'.format(ano))
else:
    print('O ano de {} não é um ano bissexto!'.format(ano))
