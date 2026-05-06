saldo = 1000
while True:
    try:
        saque = float(input("\nQual valor do saque: "))
        if saque <= 0:
            print("\nValor de saque inválido!")
            break
        elif saque > saldo:
         print("\nSaldo insuficiente")
         break
        saldo = saldo - saque
    except (ValueError, TypeError):
            print('Erro! Insira um número válido!')
    except KeyboardInterrupt:
        print("\n\nO usuário finalizou o programa!")
    except Exception as e:
        print(f'Ops! Erro do tipo: \n{e}')
    else:
        print(f'\nSaque de R${saque} realizado com sucesso, seu saldo está em: R${saldo}')
    
    try:
        resp = int(input("\nDigite qualquer tecla para continuar. Digite 0 para sair: "))
        if resp == 0:
            break
    except (ValueError, TypeError):
            print('')
    
    
    
print("\nPrograma encerrado!")


