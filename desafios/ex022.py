from itertools import count


nome=str(input('Qual é seu nome completo? ')).strip()
print('Com todas as letras maiúsculas o nome fica: {}'.format(nome.upper()))
print('Com todas as letras minúsculas o nome fica: {}'.format(nome.lower()))
dividido=nome.split()
tudo=''.join(dividido)
print('Seu nome tem ao todo {} letras'.format(len(tudo)))
print('A quantidade de letras do primeiro nome é {}'.format(len(dividido[0])))
