import math
import numpy as np


def g(x):
    # Defina uma função
    # Exemplo:
    return x**2 + math.log(x, math.e)


def secante(f, x0, x1, erro, itmax):
    # Retornará a raíz, o erro e as iterações.
    # Código feito com base no canal do Professor REX.

    it = 0
    er = 10**4
    xa1 = x0
    x = x1
    while er > erro and it < itmax:
        xa2 = xa1
        xa1 = x
        x = xa1 - f(xa1)*(xa2-xa1)/(f(xa2) - f(xa1))
        er = np.abs((x-xa1)/x)
        it += 1
    return f'raíz: {x}, Erro: {er}, Iterações: {it}'

# Exemplo de chamada da função abaixo:


print(secante(g, 0.1, 10, 0.0001, 30))
