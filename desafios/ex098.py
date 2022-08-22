from time import sleep


def contador (inicio, fim, passo = 1) :
    """
    Faz uma contagem e mostra na tela
    :parametro i: Início da contagem
    :parametro f: Fim da contagem
    :parametro p: passo da contagem
    se passo == 0 ou em branco irá se tornar 1
    :return: sem retorno   
    """
    if passo < 0 :
        passo *= -1
    elif passo == 0 :
        passo = 1
    print (f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    if inicio < fim :
        for i in range (inicio, fim + 1, passo) :
            print (i, end=' ', flush=True)
            sleep (0.5)
        print ('FIM!!!')
    elif inicio > fim :
        for i in range (inicio, fim - 1, -passo) :
            print (i, end=' ', flush=True)
            sleep (0.5)
        print ('FIM!!!')


contador (1, 10, 1)
contador (10, 0, 2)
print ('Agora é sua vez de personalizar a contagem!')
contador (int ( input ('Início: ')), int ( input ('Fim: ')), int ( input ('Passo: ')))