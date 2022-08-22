pessoas = { 'nome': 'Mateus', 'sexo': 'Masculino', 'idade': 21 }
print (f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')
pessoas ['peso'] = 50
print (pessoas.keys())
print (pessoas.values())
print (pessoas.items())
del pessoas ['sexo']
pessoas ['nome'] = 'Adrielly'
for k in pessoas.keys() :
    print (k)
for k, v in pessoas.items() :
    print (f'{k} = {v}')
