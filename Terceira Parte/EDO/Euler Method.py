# made by Leonardo Saads
import numpy as np
import matplotlib.pyplot as plt


def f(x, y):
    """
    Implementa a função (uma EDO) que o método de Euler deve ser utilizado.
    """
    # Exemplo: dy/dx = 12 - y + 2*x
    return 12 - y + 2*x


def euler(x_begin: float, y_begin: float, h: float, iteracoes: int, visualizar=False):
    """Implementa o método de Euler"""
    # f(x + h) = f(x) + f'(x,y) * h
    vetor_x = np.linspace(x_begin, x_begin + iteracoes * h, iteracoes + 1)  # cria vetor X -  OBS: iteracoes + 1
    vetor_y = vetor_x.copy()  # cria o vetor Y a partir do vetor x (valores errados)
    vetor_y[0] = y_begin  # Coloca o velor incial do vetor Y
    for i in range(1, len(vetor_y)):  # Começa em 1 () e vai até o final do vetor
        vetor_y[i] = vetor_y[i-1] + f(vetor_x[i-1], vetor_y[i-1])*h  # Calcula valores corretos do vetor Y
    if visualizar is False:
        return vetor_x, vetor_y
    elif visualizar is True:  # Possibilidade de visualizar o gráfico com matplotlib
        plt.plot(vetor_x, vetor_y, label='Euler aproximation method')
        plt.grid(True)
        plt.legend()
        plt.show()
        return vetor_x, vetor_y


# Exemplo de chamada da função
if __name__ == '__main__':
    x0 = 0
    y0 = 50
    particao = 0.5
    n = 100

    vetorx, vetory = euler(x0, y0, particao, n)
    print(vetorx)
    print(vetory)

    x0 = 161.9
    y0 = 340
    particao = 0.03
    n = 100

    vetorx, vetory = euler(x0, y0, particao, n, True)
    print(vetorx)
    print(vetory)
