# import matplotlib.pyplot as plt


# Classe dos Erros
class ValorNegativoError(Exception):
    def __init__(self):
        super().__init__("Erro de Valor Menor ou Igual a Zero")


class CircuitoRLC:
    """
    Implementa a classe do circuito RLC;
    OBS: fonte de tensão no sistema nulo;
    """

    def __init__(self, resistencia: float, indutor: float, capacitor: float):
        if resistencia <= 0 or indutor <= 0 or capacitor <= 0:
            raise ValorNegativoError
        else:
            self.res = resistencia
            self.ind = indutor
            self.cap = capacitor

    @property
    def informacoes_sistema(self):
        return self.res, self.ind, self.cap

    def lambdas(self):
        lambda1 = (-(self.res/self.ind) + ((self.res/self.ind)**2 - 4*(1/(self.ind*self.cap)))**(1/2))/2
        lambda2 = (-(self.res/self.ind) - ((self.res/self.ind)**2 - 4*(1/(self.ind*self.cap)))**(1/2))/2
        return lambda1, lambda2

    def grafico(self, valor_inicial_funcao: float, valor_inicial_derivada: float):
        pass


if __name__ == '__main__':
    circuito_teste = CircuitoRLC(3, 3, 0)
    lambdas_teste = CircuitoRLC.lambdas(circuito_teste)
    print(lambdas_teste)
