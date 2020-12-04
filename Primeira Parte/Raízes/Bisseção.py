import numpy as np
import math as mt


def g(x):
    # Defina uma função
    # Exemplo:
    return mt.log10(x**2)


def bisseccao(f, a, b, erro, iteracoes):
    # Retornará a raíz, o erro e as iterações.
    # Código feito com base no canal do Professor REX.

    it = 0
    x = b
    er = 10**4
    while er >= erro and it < iteracoes:
        xold = x
        x = (a + b)/2
        er = np.abs((x - xold)/x)
        if f(a) * f(x) < 0:
            b = x
        if f(b) * f(x) < 0:
            a = x
        if f(a) * f(b) > 0:
            return 'Não é possível aplicar o método da Bisseção neste intervalo', er, it
        it += 1
    return f'raíz: {x}, Erro: {er}, Iterações: {it}'

# Exemplo de chamada da função abaixo:


print(bisseccao(g, 0.05, 10, 0.00001, 50))
