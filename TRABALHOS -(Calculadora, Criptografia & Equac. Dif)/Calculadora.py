#  Made by Leonardo Saads

class Calculadora:
    """
    Implementa a classe de uma calculadora.
    """

    def __init__(self):
        self.e = 2.7182818284590452353602  # Numero de Neper
        self.pi = 3.1415926535897932384626  # Número Pi
        self.ouro = 1.6180339887498948482045  # Número e Ouro
        self.catalan = 0.9159655941772190150546  # Número de Catalan
        self.c_ms = 299792458  # Velocidade da Luz no Vácuo - m/s
        self.c_kms = 1079252849  # Velocidade da Luz no Vácuo - km/h

    @staticmethod
    def soma(a: float, b: float):
        """Soma dois números."""
        return a+b

    @staticmethod
    def subtracao(a: float, b: float):
        """subtrai dois números."""
        return a-b

    @staticmethod
    def multiplicacao(a: float, b: float):
        """Multiplica dois números."""
        return a*b

    @staticmethod
    def divisao(a: float, b: float):
        """Divisão de dois números."""
        if b == 0:
            raise ZeroDivisionError("Divisão por zero - Inválida.")
        else:
            return a/b

    @staticmethod
    def potencia(a: float, b: float):
        """Eleva o número 'a' pela potência 'b'."""
        return a**b

    @staticmethod
    def somatorio(*args):
        """Retorna o somatório dos dados"""
        soma = 0
        for numero in args:
            soma += float(numero)
        return soma

    @staticmethod
    def media(*args):
        """Retorna a média dos dados"""
        soma_total = Calculadora.somatorio(*args)
        quantidade = len(args)
        return soma_total/quantidade

    @staticmethod
    def variancia(*args):
        """Retorna a variância dos dados"""
        media = Calculadora.media(*args)
        variancia = 0
        for valor in args:
            variancia += Calculadora.potencia((valor - media), 2)
        return variancia/len(args)


if __name__ == '__main__':
    print(Calculadora.variancia(63, 60, 59, 55, 62))
