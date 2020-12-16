# Made by Leonardo Saads 
import matplotlib.pyplot as plt
import math
import numpy as np


# Classe dos Erros
class ValorNegativoError(Exception):
    def __init__(self):
        super().__init__("Erro de Valor Menor ou Igual a Zero")


class CircuitoRLC:
    """
    Implementa a classe do circuito RLC;
    OBS: fonte de tensão no sistema nulo;
    """

    def __init__(self, resistencia: float, indutor: float, capacitor: float, valorinicial: float, valorinicial2: float):
        if resistencia <= 0 or indutor <= 0 or capacitor <= 0:
            raise ValorNegativoError
        else:
            self.res = resistencia
            self.ind = indutor
            self.cap = capacitor
            self.y_0 = valorinicial
            self.y1_0 = valorinicial2

    def __repr__(self):
        return f'------- SISTEMA RLC -------\n' \
               f'Valor da Resistência: {self.res}\n' \
               f'Valor do Indutor: {self.ind}\n' \
               f'Valor do Capacitor: {self.cap}\n' \
               f'Condições Iniciais do Sistema' \
               f'f(0) = {self.y_0}\n' \
               f'f`(0) = {self.y1_0}\n'

    def lambdas(self):
        """
        implelemnta o cálculo das raízes
        :return: raízes
        """
        lambda1 = (-(self.res/self.ind) + ((self.res/self.ind)**2 - 4*(1/(self.ind*self.cap)))**(1/2))/2
        lambda2 = (-(self.res/self.ind) - ((self.res/self.ind)**2 - 4*(1/(self.ind*self.cap)))**(1/2))/2
        return lambda1, lambda2

    def funcao(self):
        """
        determina a funcao a ser utilizada
        :return: funcao
        """
        raiz1, raiz2 = CircuitoRLC.lambdas(self)

        if raiz1 == raiz2:
            return lambda t: self.y_0*math.e**(raiz1*t) + (self.y1_0 - self.y_0*raiz1)*t*math.e**(raiz2*t)
        if raiz1 != raiz2 and type(raiz2) == float:
            coef_2 = (self.y1_0 - self.y_0 * raiz1) / (raiz2 - raiz1)
            coef_1 = (self.y1_0 - self.y_0 * raiz2) / (raiz1 - raiz2)
            return lambda t: coef_1*math.e**(raiz1*t) + coef_2*math.e**(raiz2*t)
        else:
            return lambda t: self.y_0*math.e**(raiz1.real*t)*math.cos(raiz1.imag*t) + \
                             ((self.y1_0+raiz2.real*self.y_0)/raiz2.imag)*math.e**(raiz2.real*t)*math.sin(raiz2.imag*t)

    def aproximacao(self, h: float, final: float):
        """
        A aproximação de uma EDO com base no método de euler.
        :return: vetor
        """
        # z'[n+1] = z[n] + h*w[i-1]
        # w'[n+1] = w[n] + h*(1/LC*z[i-1] -R/C*w[i-1])
        # y(0) = z(0) & y'(0) = w(0)
        z = np.zeros(len(np.arange(0, final, h)))  # um vetor de zeros
        w = np.zeros(len(np.arange(0, final, h)))  # um vetor de zeros
        z[0] = self.y_0  # valor inicial
        w[0] = self.y1_0  # valor incial
        for i in range(1, int(final/h)):
            z[i] = z[i-1] + h*w[i-1]
            w[i] = w[i-1] + h*((-1/(self.ind*self.cap))*z[i-1] - (self.res/self.ind)*w[i-1])
        return z, w

    def grafico(self, largura: int):
        """
        implementa o gráfico
        :largura: a largura do gráfico.
        :return: gráfico
        """
        # Parte de vetores - Analítico
        funcao = CircuitoRLC.funcao(self)
        x = np.linspace(0, largura, 10000)  # PARTIÇÃO PADRÃO DE 10000
        y_x = [funcao(t) for t in x]

        # Parte de vetores - aproximações de euler
        aproximacoes = CircuitoRLC.aproximacao(self, 0.05, largura)[0]   # DETERMINE AQUI A PRECISÃO DA APROXIMAÇÃO
        x_aproc = np.linspace(0, largura, len(aproximacoes))

        # Partes gráficas
        plt.plot(x, y_x, label='EDO analytical solution')
        plt.plot(x_aproc, aproximacoes, label='Euler method aproximation')
        plt.xlabel('Tempo t')
        plt.ylabel('Carga Q(t)')
        plt.legend()
        plt.grid(True)
        plt.show()


# exemplo de chamada da classe.
if __name__ == '__main__':
    r = float(input("Detemine o valor da Resisitencia: \n"))
    ind = float(input("Detemine o valor da Indutância: \n"))
    c = float(input("Detemine o valor do Capacitor: \n"))
    y0 = float(input("determine as condições iniciais do Sistema - y(0): \n"))
    y10 = float(input("determine as condições iniciais do Sistema - y'(0): \n"))
    circuito_teste = CircuitoRLC(r, ind, c, y0, y10)
    print('Raízes do polinômio caracterítico')
    print(circuito_teste.lambdas())
    circuito_teste.grafico(35)
