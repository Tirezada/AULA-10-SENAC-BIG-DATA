#TRATAMENTO COM ELSE

print("=== Cálculo de Produtividade ===")

try:
    total_produzido = float(input('Valor total da venda: '))
    funcionarios = int(input("Total de Funcionários: "))
    
    media_por_funcionario = total_produzido / funcionarios
except (ValueError, TypeError):
    print('O valor precisa ser numérico')
except ZeroDivisionError:
    print("Erro! Informe um número válido de funcionários!")
#SE NÃO DER ERRO, ELSE É EXECUTADO
else:
    print(f'Média por funcionário: {media_por_funcionario:.2f}')
