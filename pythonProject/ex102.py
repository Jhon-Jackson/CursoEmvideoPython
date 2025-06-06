# Exercício Python 102:
# Crie um programa que tenha uma função fatorial() que receba dois
# parâmetros: o primeiro que indique o número a calcular e outro
# chamado show, que será um valor lógico (opcional)
# indicando se será mostrado ou não na tela o processo de cálculo do
# fatorial.


def fatorial(N1, show=False):
    """
    → Faz o fatorimento de um numero:
    :param N1: Elemento principal
    :return: retorna o resultado
    """
    f = 1
    for c in range(N1, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f



print('<<<Calculando Fatorial>>>')
N1  =  int(input('Diga um numero: '))
R1 = fatorial(N1,show=True)

print(R1)

