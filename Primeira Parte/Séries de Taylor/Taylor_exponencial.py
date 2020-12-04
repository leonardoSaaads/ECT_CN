import math


def taylor_exp(x0: float, x: float, n: int):
    """
    Aproximará a função e^x pela série de Taylor.
    x0 -> ponto incial.
    x -> ponto para aproximação.
    n -> número de termos.
    """
    soma = 0
    for i in range(n):
        soma += math.e ** x0 * ((x - x0) ** i) / math.factorial(i)
    return soma
