from datetime import date
sexo=str(input('Qual seu sexo?\n [ M ] Masculino\n [ F ] Feminino\n Opção: ')).lower().strip()
if sexo == 'f':
    print('Você não precisa comparecer ao alistamento militar obrigatório!')
else:
    ano=int(input('Em qual ano você nasceu? '))
    idade=date.today().year-ano
    atual=date.today().year
    print(f'Quem nasceu em {ano} tem {idade} anos em {atual}')
    if idade <= 17:
        print(f'Ainda não chegou a hora de você se alistar ao serviço militar, lhe falta(m) {18-idade} ano(s).')
    elif idade == 18:
        print('Parabéns! chegou a hora de fazer o seu alistamento militar, dirija-se a junta militar mais próxima para receber maiores informações.')
    else:
        print(f'Já passou da hora de se alistar pois você já está atrasado em {(18-idade)*-1} ano(s), dirija-se a junta militar mais próxima para por em dia sua documentação!')
