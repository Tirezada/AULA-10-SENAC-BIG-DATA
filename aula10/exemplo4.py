#TRATAMENTO COM FINALLY
print("=== Cálculo de Produtividade ===")

try:
    total_produzido = float(input('\nValor total da venda: '))
    funcionarios = int(input("Total de Funcionários: "))
    
    media_por_funcionario = total_produzido / funcionarios
except (ValueError, TypeError):
    print('O valor precisa ser numérico')
except ZeroDivisionError:
    print("Erro! Informe um número válido de funcionários!")
else:
    print(f'Média por funcionário: {media_por_funcionario:.2f}')
#SERÁ EXECUTADO SE DER ERRO OU NÃO
finally:
    print("\n=== Programa encerrado ===")