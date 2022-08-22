d=int(input('Por quantos dias o carro ficou alugado? '))
k=float(input('Quantos kilometros foram rodados? '))
pd=d*60
pk=k*0.15
pf=pd+pk
print(f'A quantidade a pagar pelos dias passados com o carro é de R${pd:.2f}')
print(f'A quantidade a pagar pelos kilometros rodados é de R${pk:.2f}')
print(f'Totalizando, devem ser pagos R${pf:.2f} pelo aluguel do carro.')
