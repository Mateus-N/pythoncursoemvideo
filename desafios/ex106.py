c = (
    '\033[0;0m',        #Remove
    '\033[1;41m',       #Vermelho
    '\033[1;42m',       #Verde
    '\033[1;43m',       #Amarelo
    '\033[1;44m',       #Azul
    '\033[1;45m',       #magenta
    '\033[1;107m'       #Branco
)

def título (texto, cor=0) :
    tam = len(texto) + 4
    print (c[cor], end='')
    print ('~'*tam)
    print (f'  {texto}  ')
    print ('~'*tam)
    print (c[0])


def ajuda (com) :
    help (com)


while True :
    título ('Sistema de ajuda PyHELP', 2)
    comando = str ( input ('Função ou biblioteca > '))
    if comando.upper == 'FIM' :
        break
    ajuda (comando)
título ('ATÉ LOGO', 1)
