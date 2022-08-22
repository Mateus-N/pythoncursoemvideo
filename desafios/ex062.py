primeirotermo = int ( input ('Primeiro termo: '))
razão = int ( input ('Razão da PA: '))
termoatual = primeirotermo
contador = 1
total = 0
termosamais = 10
while termosamais != 0 :
    total += termosamais
    while contador <= total :
        print (f'{termoatual} -> ', end='')
        termoatual += razão
        contador += 1
    print ('PAUSA')
    termosamais = int ( input ('Quantos termos você quer mostra a mais? '))
print (f'Progressão finalizada com um total de {total} termos')
