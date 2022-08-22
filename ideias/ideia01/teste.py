def calculadora () :
  '''
    -> Função para realizar as operações de soma, subtração, divisão, e multiplicação
  '''
  # Recebe os valores
  numero1 = int ( input ('Digite o primeiro valor: '))
  numero2 = int ( input ('Digite o segundo valor: '))

  # Seleção do operador matemático
  print ('O que você deseja fazer?\n 1 - Somar\n 2 - Subtrair\n 3 - Multiplicar\n 4 - Dividir')
  opcao = int ( input ('Opção: '))

  # Realiza a soma
  if opcao == 1 :
    print (f'A soma vale {int (numero1) + int (numero2)}')

  # Realiza a subtração
  elif opcao == 2 :
    print (f'A subtração vale {int (numero1) - int (numero2)}')

  # Realiza a multiplicação
  elif opcao == 3 :
    print (f'O produto vale {int (numero1) * int (numero2)}')

  # Realiza a divisão
  elif opcao == 4 :
    # Caso o segundo número for 0 a divisão não é realizada por ser matemáticamente impossível
    if numero2 == 0 :
      print ('Não é possível dividir por 0')
    else :
      print (f'A divisão vale {int (numero1) / int (numero2)}')


calculadora()
