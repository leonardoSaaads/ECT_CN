import math
import numpy as np


def g(x):
    # Defina uma função
    # Exemplo:
    return x**2 + math.log(x, math.e)


def dg(x):
    # Coloque a derivada da função
    return 2*x + 1/x


def newton(f, df, x0, erro, itmax):
    # Retornará a raíz, o erro e as iterações.
    # Código feito com base no canal do Professor REX.

    it = 0
    er = 10**8  # Erro muito alto
    x = x0
    while er > erro and it < itmax:
        xold = x
        x = x - f(x)/df(x)
        er = np.abs((x-xold)/x)
        it += 1
    return f'raíz: {x}, Erro: {er}, Iterações: {it}'

# Exemplo de chamada da função abaixo:


print(newton(g, dg, 0.8, 0.00001, 10))
