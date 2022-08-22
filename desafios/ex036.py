val=float(input('Qual o valor da casa? '))
sal=float(input('Salário do comprador? '))
anos=int(input('Em quantos anos pretente pagar? '))
pm=val/(anos*12)
emprestimo='pode ser CONCEDIDO!'
if pm > sal/100*30:
    emprestimo='NEGADO'
print(f'Para pagar uma casa de R${val:.2f} em {anos} ano(s) serão {anos*12} parcelas no valor de R${pm:.2f} \n Empréstimo {emprestimo}')
