import numpy as np
import math


def g(x):
    # Defina uma função
    # Exemplo:
    return x ** 2 + math.log(x, math.e)


def falsaposicao(f, a, b, erro, iteracoes):
    # Retornará a raíz, o erro e as iterações.
    # Código feito com base no canal do Professor REX.

    it = 0
    x = a
    er = 10**4
    while er >= erro and it < iteracoes:
        xold = x
        x = a - f(a)*(b-a)/(f(b) - f(a))
        er = np.abs((x - xold)/x)
        if f(a) * f(x) < 0:
            b = x
        if f(b) * f(x) < 0:
            a = x
        if f(a) * f(b) > 0:
            return 'Não é possível aplicar o método da Falsa-Posição neste intervalo', er, it
        it += 1
    return f'raíz: {x}, Erro: {er}, Iterações: {it}'

# Exemplo de chamada da função abaixo:


print(falsaposicao(g, 0.1, 10, 0.0001, 30))
