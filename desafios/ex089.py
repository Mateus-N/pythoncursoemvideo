alunos = []
contador = 0
while True :
    alunos.append([])
    alunos[contador].append ( str ( input ('Nome: ')))
    alunos[contador].append ([])
    alunos[contador][1].append ( float ( input ('Nota 1: ')))
    alunos[contador][1].append ( float ( input ('Nota 2: ')))
    contador += 1
    while True :
        continuar = str ( input ('Quer continuar [S/N] ? '))[0]
        if continuar in 'nNsS' :
            break
    if continuar in 'nN' :
        break
contador = 0
print ('-='*20)
print (f'{"No.":<5} {"Nome":<20} Média')
print ('-'*40)
for i in alunos :
    média = (alunos[contador][1][0]+alunos[contador][1][1])/2
    print (f'{contador:<5} {alunos[contador][0]:<20} {média:.1f}')
    contador += 1
print ('-'*40)
while True:
    mostrarnotas = int ( input ('Mostrar notas de qual aluno (999 interrompe) : '))
    if mostrarnotas == 999 :
        break
    print (f'A médias do aluno {alunos[mostrarnotas][0]} são {alunos[mostrarnotas][1][0]} e {alunos[mostrarnotas][1][1]}.')
    print ('-'*40)
print ('''FINALIZANDO...
<<< VOLTE SEMPRE >>>''')
