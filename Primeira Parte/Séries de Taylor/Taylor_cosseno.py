import math


def taylor_cosseno1(x0: float, x: float, n: int):
    """
    Aproximará a função cos(x) pela série de Taylor.
    x0 -> ponto incial.
    x -> ponto para aproximação.
    n -> número de termos.
    """
    soma = 0
    for num in range(n):
        if num % 4 == 3:
            soma += math.sin(x0) * ((x - x0) ** num) / math.factorial(num)
        if num % 4 == 0:
            soma += math.cos(x0) * ((x - x0) ** num) / math.factorial(num)
        if num % 4 == 1:
            soma += -math.sin(x0) * ((x - x0) ** num) / math.factorial(num)
        if num % 4 == 2:
            soma += -math.cos(x0) * ((x - x0) ** num) / math.factorial(num)
    return soma
