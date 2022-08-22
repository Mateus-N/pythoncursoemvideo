from datetime import date
cadastro = {}
cadastro['nome'] = str ( input ('Nome: '))
nascimento = int ( input ('Ano de nascimento: '))
cadastro['idade'] = date.today().year - nascimento
cadastro['ctps'] = int ( input ('Carteira de trabalho (0 Não tem): '))
if cadastro['ctps'] != 0 :
    cadastro['contratação'] = int ( input ('Ano de contratação: '))
    cadastro['salário'] = float ( input ('Salário: R$'))
    cadastro['aposentadoria'] = cadastro['contratação'] - nascimento + 35
for k, v in cadastro.items() :
    print (f'   -{k} tem o valor {v}')
