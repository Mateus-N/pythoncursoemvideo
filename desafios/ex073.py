times = ('Palmeiras', 'Athletico-PR', 'Atlético-MG', 'Corinthians', 'Internacional', 'Fluminense', 'São Paulo', 'Flamengo', 'Botafogo', 'Santos', 'Avaí', 'Coritiba', 'América-MG', 'Bragantino', 'Ceará SC', 'Atlético-GO', 'Goiás', 'Cuiabá', 'Juventude', 'Fortaleza')

print (f'Os cinco primeiros colocados são ', end='')
for time in times [:5] :
    print (time, end=' -> ')
print ('\n')

print (f'Os ultimos quatro colocados são ', end='')
for timefinal in times [-4:] :
    print (timefinal, end=' -> ')
print ('\n')

print (f'Os times em ordem alfabética: ', end='')
ordem = sorted(times)
for lista in ordem :
    print(lista, end=' -> ')
print ('\n')

print (f'O santos está na {times.index("Santos")+1}ª posição da tabela.')
