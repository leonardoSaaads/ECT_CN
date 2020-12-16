# made by Leonardo Saads
import matplotlib.pyplot as plt
import math
import numpy as np


# Classe dos Erros
class ValorNegativoError(Exception):
    def __init__(self):
        super().__init__("Erro de Valor Menor ou Igual a Zero")


class Oscilador:
    """
    Implementa a classe do Oscilador Harmônico Amortecido
    """

    def __init__(self, m: float, u: float, k: float, x_inicial: float, v_inicial):
        """
        Adquire os parâmetros da classe.
        :param m: massa
        :param u: constante positiva
        :param k: constante elástica
        :param x_inicial: espaço inicial
        :param v_inicial: valocidade inicial
        """
        if m <= 0 or u <= 0 or k <= 0:
            raise ValorNegativoError
        else:
            self.m = m
            self.u = u
            self.k = k
            self.space = x_inicial
            self.velocity = v_inicial

    def __repr__(self):
        """
        Representação.
        :return: string
        """
        return f'------- SISTEMA OSCILADOR -------\n' \
               f'Valor da Massa: {self.m}\n' \
               f'Valor do U: {self.u}\n' \
               f'Valor do K: {self.k}\n' \
               f'Condições Iniciais do Sistema' \
               f'f(0) = {self.space}\n' \
               f'f`(0) = {self.velocity}\n'

    def lambdas(self):
        """
        Implelemta o cálculo das raízes dos polinômio característico.
        :return: lambda1, lambda2
        """
        v = (self.u/self.m)/2
        w = (self.k/self.m)**(1/2)
        lambda1 = (v**2 - w**2)**(1/2) - v
        lambda2 = - (v**2 - w**2)**(1/2) - v
        return lambda1, lambda2

    def funcao(self):
        """
        determina a funcao a ser utilizada
        :return: funcao
        """
        raiz1, raiz2 = Oscilador.lambdas(self)

        if raiz1 == raiz2:
            return lambda t: self.space*math.e**(raiz1*t) + (self.velocity - self.space*raiz1)*t*math.e**(raiz2*t)
        if raiz1 != raiz2 and type(raiz2) == float:
            coef_2 = (self.velocity - self.space * raiz1) / (raiz2 - raiz1)
            coef_1 = (self.velocity - self.space * raiz2) / (raiz1 - raiz2)
            return lambda t: coef_1*math.e**(raiz1*t) + coef_2*math.e**(raiz2*t)
        else:
            return lambda t: self.space*math.e**(raiz1.real*t)*math.cos(raiz1.imag*t) + \
                             ((self.velocity+raiz2.real*self.space)/raiz2.imag)*math.e**(raiz2.real*t) *\
                             math.sin(raiz2.imag*t)

    def aproximacao(self, h: float, final: float):
        """
        A aproximação de uma EDO com base no método de euler.
        :return: vetor
        """

        # z'[n+1] = z[n] + h*w[i-1]
        # w'[n+1] = w[n] + h*(-2v*w[n] - w**2 z[n])
        # y(0) = z(0) & y'(0) = w(0)

        # defininindo z e w
        v = (self.u / self.m) / 2
        g = (self.k / self.m) ** (1 / 2)

        z = np.zeros(len(np.arange(0, final, h)))  # um vetor de zeros
        w = np.zeros(len(np.arange(0, final, h)))  # um vetor de zeros
        z[0] = self.space  # valor inicial
        w[0] = self.velocity  # valor incial
        for i in range(1, int(final/h)):
            z[i] = z[i-1] + h*w[i-1]
            w[i] = w[i-1] + h*((-2*v)*z[i-1] - (g**2)*w[i-1])
        return z, w

    def grafico(self, largura: int):
        """
        implementa o gráfico
        :largura: a largura do gráfico.
        :return: gráfico
        """

        # parte de vetores - aproximações e euler
        aproximacoes = Oscilador.aproximacao(self, 0.05, largura)[0]   # DETERMINE AQUI A PRECISÃO DA APROXIMAÇÃO
        x_aproc = np.linspace(0, largura, len(aproximacoes))

        # Partes gráficas
        plt.plot(x_aproc, aproximacoes, label='Euler method aproximation')
        plt.xlabel('Tempo t')
        plt.ylabel('Space x(t)')
        plt.legend()
        plt.grid(True)
        plt.show()


# exemplo de chamada da classe
if __name__ == '__main__':
    mass = float(input("Detemine o valor da Massa: \n"))
    uconst = float(input("Detemine o valor da U: \n"))
    kconst = float(input("Detemine o valor do K: \n"))
    y0 = float(input("determine as condições iniciais do Sistema - y(0): \n"))
    y10 = float(input("determine as condições iniciais do Sistema - y'(0): \n"))
    oscilador_teste = Oscilador(mass, uconst, kconst, y0, y10)
    print('Raízes do polinômio caracterítico')
    print(oscilador_teste.lambdas())
    oscilador_teste.grafico(30)
