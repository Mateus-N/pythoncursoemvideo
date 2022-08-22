def notas (*notas, sit = False) :
    """
        -> Função para analisar notas e situações de vários alunos.
        :paremetro notas: uma ou mais notas de alunos (aceita várias)
        :parametro sit: valor opcional, indicado se deve ou não adicionar a situação
        :return: dicionário com várias informações sobre a situação da turma.
    """
    dados = {}
    maior = menor = média = 0
    for c, i in enumerate(notas) :
        média += i
        if c == 0 :
            maior = menor = i
        elif i > maior :
            maior = i
        elif i < menor :
            menor = i
    média /= len(notas)
    dados['total'] = len(notas)
    dados['maior'] = maior
    dados['menor'] = menor
    dados['média'] = média
    if sit :
        if média >= 7 :
            dados['situação'] = 'BOA'
        elif média >= 5 :
            dados['situação'] = 'RAZOÁVEL'
        else:
            dados['situação'] = 'RUIM'
    return dados


resp = notas (5.5, 9.5, 10, 6.5, sit=True)
print (resp)
help (notas)
