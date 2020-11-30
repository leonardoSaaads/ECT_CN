#  Made by Leonardo Saads
import math


class Calculadora:
    """
    Implementa a classe de uma calculadora.
    """

    e = 2.7182818284590452353602  # Numero de Neper
    pi = 3.1415926535897932384626  # Número Pi
    ouro = 1.6180339887498948482045  # Número e Ouro
    catalan = 0.9159655941772190150546  # Número de Catalan
    c_ms = 299792458  # Velocidade da Luz no Vácuo - m/s
    c_kms = 1079252849  # Velocidade da Luz no Vácuo - km/h

    @staticmethod
    def soma(a: float, b: float):
        """
        Soma dois números.
        """
        return a+b

    @staticmethod
    def subtracao(a: float, b: float):
        """
        subtrai dois números.
        """
        return a-b

    @staticmethod
    def multiplicacao(a: float, b: float):
        """
        Multiplica dois números.
        """
        return a*b

    @staticmethod
    def divisao(a: float, b: float):
        """
        Divisão de dois números.
        """
        if b == 0:
            raise ZeroDivisionError("Divisão por zero - Inválida.")
        else:
            return a/b

    @staticmethod
    def potencia(a: float, b: float):
        """
        Eleva o número 'a' pela potência 'b'.
        """
        return a**b

    @staticmethod
    def roll(*args):
        """Retorna roll de vários dados - ou seja, organiza do menor para o maior"""
        return sorted(args)

    @staticmethod
    def mediana(*args):
        dados = Calculadora.roll(*args)
        numero = int(len(args)/2)
        if numero % 2 == 1:
            return dados[numero]
        if numero % 2 == 0:
            return (dados[numero-1] + dados[numero])/2

    @staticmethod
    def somatorio(*args):
        """
        Retorna o somatório dos dados.
        """
        soma = 0
        for numero in args:
            soma += float(numero)
        return soma

    @staticmethod
    def media(*args):
        """
        Retorna a média dos dados.
        """
        soma_total = Calculadora.somatorio(*args)
        quantidade = len(args)
        return soma_total/quantidade

    @staticmethod
    def variancia(*args):
        """
        Retorna a variância dos dados.
        """
        media = Calculadora.media(*args)
        variancia = 0
        for valor in args:
            variancia += Calculadora.potencia((valor - media), 2)
        return variancia/len(args)

    @staticmethod
    def desv_padrao(*args):
        """
        Retorna o desvio padrão dos dados.
        """
        variancia = Calculadora.variancia(*args)
        return Calculadora.potencia(variancia, (1/2))

    @staticmethod
    def fatorial(n: int):
        """
        Retorna o fatorial de um número inteiro positivo.
        """
        produtorio = 1
        if n >= 0:
            for numero in range(1, n+1):
                produtorio *= numero
        else:
            raise ValueError("O número deve ser um inteiro maior ou igual a 0")
        return produtorio

    @staticmethod
    def taylor_exp(x0: float, x: float, n: int):
        """
        Aproximará a função e^x pela série de Taylor.
        x0 -> ponto incial.
        x -> ponto para aproximação.
        n -> número de termos.
        """
        soma = 0
        for i in range(n):
            soma += Calculadora.e ** x0 * ((x - x0) ** i) / Calculadora.fatorial(i)
        return soma

    @staticmethod
    def taylor_seno(x0: float, x: float, n: int):
        """
        Aproximará a função sin(x) pela série de Taylor.
        x0 -> ponto incial.
        x -> ponto para aproximação.
        n -> número de termos.
        """
        soma = 0
        for num in range(n):
            if num % 4 == 0:
                soma += math.sin(x0) * ((x - x0) ** num) / math.factorial(num)
            if num % 4 == 1:
                soma += math.cos(x0) * ((x - x0) ** num) / math.factorial(num)
            if num % 4 == 2:
                soma += -math.sin(x0) * ((x - x0) ** num) / math.factorial(num)
            if num % 4 == 3:
                soma += -math.cos(x0) * ((x - x0) ** num) / math.factorial(num)
        return soma

    @staticmethod
    def taylor_cosseno(x0: float, x: float, n: int):
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
    

if __name__ == '__main__':
    # Para chamar a função, utilize a classe Calculadora.

    # Exemplo 1:
    print(Calculadora.potencia(2, 3))

    # Exemplo 2:
    print(Calculadora.desv_padrao(59, 60, 63, 60, 58, 60, 60))
