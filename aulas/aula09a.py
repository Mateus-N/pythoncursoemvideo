frase='    Curso em Vídeo Python    '
print(frase[4:9])
print("""Aqui nós temos um grande texto que está sendo feito apenas para exemplo.
pular linhas e outras formatações funcionam nesse modelo
como você pode ver aqui.""")
print(frase.upper().count('O'))
print(len(frase.strip()))
print(frase.strip().replace('Python','Android'))
print('Curso' in frase)
print(frase.find('Vídeo'))
print(frase.strip().upper())
print(frase.lower())
print(frase.split())
dividido=frase.replace('Python','Java').split()
print(dividido[3])
print(dividido[2][2:])
