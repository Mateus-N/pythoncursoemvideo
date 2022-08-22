altura=float(input('Qual é sua altura (em metros)? '))
peso=float(input('Qual é seu peso (em quilos)? '))
imc=peso/altura**2
status=('abaixo do peso, é aconselhado a procura um médico.')
if 18.5<=imc<=25:
    status=('com o peso ideal, parabéns!')
elif 25<imc<=30:
    status=('com sobrepeso, cuidado, é aconselhado a procurado de um médico')
elif 30<imc<=40:
    status=('com obesidade, tenha muito cuidado e procure um médico imediatamente!')
elif 40<imc:
    status=('com obesidade mórbida, procure um médico com extrema urgência!')
print(f'Seu IMC é de {imc:.2f} e você está {status}!')
