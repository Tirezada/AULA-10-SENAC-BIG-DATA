def media(a,b,c,d):
    return (a + b + c + d) / 4

cont = 1
alunos = []
while True:
    aluno = {}

    try:
        aluno['nome'] = input("\nQual seu nome: ")
        aluno['nota1'] = int(input("\nPrimeira nota: "))
        aluno['nota2'] = int(input("Segunda nota: "))
        aluno['nota3'] = int(input("Terceira nota: "))
        aluno['nota4'] = int(input("Quarta nota: "))
    except ValueError:
        print('Erro: Informe apenas valores válidos!')
    alunos.append(aluno)
    
    resp = input("\nDeseja continuar?").upper().strip()[0]

    if resp == 'N':
        break

for i in alunos:
    try:
        print(f'\n{i['nome']}:')
        resposta = media(i['nota1'], i['nota2'], i['nota3'], i['nota4'])
        print(f'Média = {resposta}:')
    except KeyError:
        print('Erro: Número de notas insuficientes!')

print('\nPrograma Encerrado!')