menu ='''
    SEJA BEM VINDO AO SEU BANCO!
      O QUE DESEJA FAZER? 
      1 - [DEPOSITAR]
      2 - [SACAR]
      3 - [EXTRATO]
      0 - [SAIR]
'''

saldo = 0
limite = 500
extrato = ''
numeros_saques = 0
LIMITE_SAQUE = 3

while True:
    print(menu)
    opcao = int(input('Selcione a opção: '))

    if opcao == 1:
        print('==============DEPOSITAR==============')
        deposito = float(input('Informe o valor do depósito: R$ '))
        if deposito > 0:
            print('Deposito feito com sucesso!!!')
            saldo += deposito
            extrato += 'Foi depositado um valor de R$ {:.2f}\n'.format(deposito)
            print('Seu saldo atual é de R$ {:.2f}'.format(saldo))
        else: 
            print('Valores negativos não podem ser depositados, TENTE NOVAMENTE!')

    elif opcao == 2: 
        print('==============SACAR==============')
        saque = float(input('Qual o valor que deseja sacar: R$ '))

        excedeu_saques = numeros_saques >= LIMITE_SAQUE

        if saque > saldo:
            print('Valor do saque é maior do que o saldo em conta')
            print('SALDO EM CONTA: RS {:.2f}'.format(saldo))
            print('TENTE NOVAMENTE')

        elif saque > 500:
             print('Saque maior que o limite maximo por saque de R$ 500.00. TENTE NOVAMENTE')

        elif saque < 0:
            print('Valores negativos não podem ser sacados, TENTE NOVAMENTE')

        elif excedeu_saques:
            print('Número maximo de saques diários excedido!')

        elif saque <= saldo and saque <= 500 and saldo > 0:
            print('Saque realizado com sucesso!!!')
            extrato += 'foi realizado um saque no valor de R$ {:.2f}\n'.format(saque)
            saldo -= saque
            numeros_saques += 1
            print('Seu saldo atual é de R$ {:.2f}'.format(saldo))
          
    elif opcao == 3:
        print('==============EXTRATO==============')
        print('Exibindo seu extrato...')
        import time

        time.sleep(1)
        print('EXTRATO: ')
        print('Não foram feitas movimentações' if not extrato else extrato)
        print('Seu saldo atual é R$ {:.2f}'.format(saldo))

    elif opcao != 0 and 1 and 2 and 3:
        print('Opção inválida, TENTE NOVAMENTE!!')

    else:
        print('Obrigado por acessar o sistema. Volte sempre')
        break
