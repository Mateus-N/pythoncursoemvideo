s=str=input('Qual seu sexo [M/F]? ')
while s not in 'MmFf':
    print('Opção inexistente, tente novamente.')
    s=str=input('Qual seu sexo [M/F]? ')
if s in 'mM':
    s='masculino'
else:
    s='feminino'
print(f'Você é do sexo {s}!')
