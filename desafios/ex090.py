aluno = {}
aluno['Nome'] = str ( input ('Nome: '))
aluno['Média'] = float ( input ('Média: '))
if aluno['Média'] >= 7 :
    aluno['Situação'] = 'Aprovado'
elif aluno['Média'] >= 5 :
    aluno['Situação'] = 'Recuperação'
else:
    aluno['Situação'] = 'Reprovado'
for k, v in aluno.items() :
    print(f'{k} é igual a {v}')
