nome=str(input('Digite seu nome completo: ')).strip()
print('Nome completo: {}'.format(nome))
dividido=nome.split()
print('Primeiro nome: {}'.format(dividido[0]))
print('Último nome: {}'.format(dividido[-1]))
