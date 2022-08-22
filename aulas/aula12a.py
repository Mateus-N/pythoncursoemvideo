nome=str(input('Qual é seu nome? '))
if nome == 'Adrielly':
    print('Que nome lindo!')
elif nome == 'Mateus':
    print('Olá mestre!')
elif nome == 'João' or nome == 'José' or nome == 'Maria' or nome == 'Pedro' or nome == 'Paulo':
    print('Seu nome é muito popular no Brasil.')
else:
    print('Que nome normal.')
print('Tenha um bom dia, {}!'.format(nome))
