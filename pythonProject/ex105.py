# Exercício Python 105:
# Faça um programa que tenha uma função notas() que pode receber
# várias notas de alunos e vai retornar um dicionário com as
# seguintes informações:
# – Quantidade de notas
# – A maior nota
# – A menor nota
# – A média da turma
# – A situação (opcional)


dado = []
def notas(*n, sit=False):
    Notas = {}
    Notas['Total'] = len(n)
    Notas['maior'] = max(n)
    Notas['menor'] = min(n)
    Notas['Media'] = sum(n)/len(n)
    if sit:
        if Notas['Media'] >=7:
            Notas['situação'] = 'BOA'
        elif Notas['Media'] >= 5:
            Notas['situação'] = 'RAZOAVEL'
        else:
            Notas['situação'] = 'RUIM'
    return Notas



No = notas(5, 5, 4,sit=True)

print(No)


