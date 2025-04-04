#Exercício Python 076:
# Crie um programa que tenha uma tupla única
# com nomes de produtos e seus respectivos
# preços, na sequência. No final, mostre uma
# listagem de preços, organizando os dados em
# forma tabular.

listagem = ('Lapis', 1.75,
            'Borracha', 2,
            'Caderno', 15.90,
            'Estojo', 25,
            'Transferidor', 4.20,
            'Compasso', 9.99,
            'Mochila', 120.32,
            'Canetas', 22.30,
            'Livro', 34.90)
print('\033[33m-\033[m'*40)
print(f'{'\033[31mLISTAGEM DE PREÇOS\033[m':^40}')
print('\033[34m-\033[m'*40)
for pos in range (0, len(listagem)):
    if pos % 2 ==0:
        print(f'\033[{(pos + 30)}m{listagem[pos]:.<30}\033[m', end='')
    else:
        print(f'\033[{30+pos}mR${listagem[pos]:>7.2f}\033[m')

print('\033[35m-\033[m'*40)
