from random import randint
tentativas=0
user=''
num=int(randint(0,10))
print('O computador escolheu um número de 0 a 10, consegue advinhar?')
while user != num:
    tentativas+=1
    user=int(input(f'{tentativas}ª Tentativa: '))
    if user > num:
        print('Menos... Tente de novo.')
    elif user < num:
        print('Mais... Tente de novo')
print(f'Parabéns, você acertou! Foram necessárias {tentativas} tentativas.')
