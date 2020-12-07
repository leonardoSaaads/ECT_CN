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
            # Necessário implementar condições iniciais
            return lambda t: self.y_0*math.e**(raiz1*t) + t*math.e**(raiz2*t)
        if raiz1 != raiz2 and type(raiz2) == float:
            # Necessário implementar condições iniciais
            return lambda t: math.e**(raiz1*t) + math.e**(raiz2*t)
        else:
            # Necessário implementar condições iniciais
            return lambda t: self.y_0*math.e**(raiz1.real*t)*math.cos(raiz1.imag*t) + \
                             math.e**(raiz2.real*t)*math.sin(raiz2.imag*t)

    def grafico(self):
        """
        implementa o gráfico
        :return: gráfico
        """
        funcao = CircuitoRLC.funcao(self)
        x = np.linspace(0, 25, 120)
        y_x = [funcao(t) for t in x]

        plt.plot(x, y_x, label='EDO analytical solution')
        plt.xlabel('Tempo t')
        plt.ylabel('Carga Q(t)')
        plt.legend()
        plt.grid(True)
        plt.show()


if __name__ == '__main__':
    circuito_teste = CircuitoRLC(1, 5, 1, 10, 1)
    print(circuito_teste.lambdas())
    circuito_teste.grafico()
