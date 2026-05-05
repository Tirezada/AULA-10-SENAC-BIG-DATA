#TRATAMENTO COM EXCEPTION
print("=== Cálculo de Produtividade ===")

try:
    total_produzido = float(input('\nValor total da venda: '))
    funcionarios = int(input("Total de Funcionários: "))
    
    media_por_funcionario = total_produzido / funcionarios
#TRATA O ERRO DE UMA FORMA GERAL, INDICANDO QUAL ERRO FOI
except Exception as e:
    print(f'Ops! Erro do tipo: \n{e}')
except KeyboardInterrupt:
    print("\n\nO usuário finalizou o programa!")

else:
    print(f'Média por funcionário: {media_por_funcionario:.2f}')
finally:
    print("\n=== Programa encerrado ===")