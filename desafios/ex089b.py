alunos = []
while True :
    nome = str ( input ('Nome: '))
    nota1 = float ( input ('Nota 1: '))
    nota2 = float ( input ('Nota 2: '))
    média = (nota1 + nota2) / 2
    alunos.append([nome, [nota1, nota2], média])
    continuar = str ( input ('Quer continuar [S/N] ? '))[0]
    if continuar in 'nN' :
        break
print ('-='*20)
print (f'{"No.":<5} {"Nome":<20} Média')
print ('-'*40)
for c, i in enumerate(alunos) :
    print (f'{c:<5} {alunos[c][0]:<20} {alunos[c][2]:.1f}')
while True:
    mostrarnotas = int ( input ('Mostrar notas de qual aluno (999 interrompe) : '))
    if mostrarnotas == 999 :
        break
    print (f'A médias do aluno {alunos[mostrarnotas][0]} são {alunos[mostrarnotas][1][0]:.1f} e {alunos[mostrarnotas][1][1]:.1f}.')
    print ('-'*40)
print ('''FINALIZANDO...
<<< VOLTE SEMPRE >>>''')
