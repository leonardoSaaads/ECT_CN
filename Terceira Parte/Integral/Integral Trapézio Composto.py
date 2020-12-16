# made by Leonardo Saads
import math

a = float(input())
b = float(input())
numero = int(input())


def particao(function, valor_a, valor_b, numero_de_particoes):
    particionar = (valor_b - valor_a) / numero_de_particoes
    criador_particao = valor_a
    criador_x = []  # cria o vetor x
    criador_y = []  # cria o vetor y
    contador = 0

    while contador <= numero_de_particoes:
        criador_x.append(criador_particao)  # adiciona as particções em x
        criador_y.append(function(float(criador_x[contador])))  # adiciona a função partição em y
        criador_particao = criador_particao + particionar
        contador = contador + 1
    return criador_x, criador_y  # Retorna a partição de x & y


# Função padrão: sin(x)
x, y = particao(math.sin, a, b, numero)
area = 0

#  Aplica o método do trapézio.
for indice in range(1, len(x)):  # Deve ser um a menos
    area = area + (float(y[indice]) + float(y[indice - 1])) * (float(x[indice]) - float(x[indice - 1])) / 2

# Precisão padrão de 8 casas decimais.
print('%.8f' % area)
