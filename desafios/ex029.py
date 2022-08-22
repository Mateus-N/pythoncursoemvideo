v=float(input('Qual a velocidade do carro? '))
multa=(v-80)*7
if v > 80:
    print('MULTADO! Você estava acima do limite de 80Km/h. O valor da multa é de R${:.2f}!'.format(multa))
    print('Mais atenção da próxima vez!')
print('Tenha um bom dia! Dirija com segurança!')
