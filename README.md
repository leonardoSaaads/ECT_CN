# COMPUTAÇÃO NÚMERICA (UFRN) - MÉTODOS NUMÉRICOS EM PYTHON 
Esse repositório é dedicado à matéria de **Computação Numérica da UFRN**. Todos os métodos foram feitos em **Python** e com base no semestre de 2020.2 da Escola de Ciências e Tecnologia.

## Métodos Numéricos - Códigos:
* [Aprendendo Python](https://github.com/leonardoSaaads/ECT_CN/blob/main/Aprendendo_Python_Basico)
* [Série de Taylor, Bolzano, Bissecção, Falsa posição, Newton & Secante](https://github.com/leonardoSaaads/ECT_CN/tree/main/Primeira%20Parte)
* [Eliminação Gauss, Decomposição LU, Jacobi Sistemas & Gauss-Seidel]()
* [Métodos Mínimos Quadrados, Interpolação de Lagrange & Interpolação de Newton]()
* [Interação, Regras de Simpson, Equações DIferenciais Ordinárias com Euler & Equações Diferenciais Odinárias com RK4]()

Para a visualização dessa biblioteca, é recomendável utilizar a biblioteca ```matplotlib```.

## Trabalhos para Submissão - Códigos & Instepretação:
* [Primeira Unidade - Calculadora](https://github.com/leonardoSaaads/ECT_CN/blob/main/TRABALHOS%20-(Calculadora%2C%20Criptografia%20%26%20Equac.%20Dif)/Calculadora.py)
* [Segunda Unidade - Criptografia em LU]()
* [Terceira Unidade - Equações Diferenciais com Aplicações](https://github.com/leonardoSaaads/ECT_CN/tree/main/TRABALHOS%20-(Calculadora%2C%20Criptografia%20%26%20Equac.%20Dif)/Trabalhos%20de%20EDO)

## Observações:
Para utilizar esse repositório, é recomendável utilizar:
* Python version > 3.6
* Numpy version > 1.19.1
* Matplotlib version >= 3.3.1

Primeiramente, utilize o comando abaixo para atualizar o [gerencimaneto de pacotes](https://pip.pypa.io/en/stable/installing/):

**Para Linux ou macOS:**
```
pip install -U pip
```
**Para Windows:**
```
python -m pip install -U pip
```

Utilize o comando abaixo para instalar a biblioteca [matplotlib](https://matplotlib.org/users/installing.html) & [numpy](https://numpy.org/install/):
```
python -m pip install -U matplotlib
python -m pip install -U numpy
```

## Contribuidores:
* [Leonardo Saads Pinto](https://github.com/leonardoSaaads)

<img style="-webkit-user-select: none;margin: auto;cursor: zoom-in;" src="https://user-images.githubusercontent.com/69808278/100530830-dd911500-31d5-11eb-9e87-8dcd51f92082.png" width="228" height="228">

# Informações Gerais:
O semestre na UFRN é divido em 3 partes. Na primeira parte é apresentado uma introdução à linguagem Python, a biblioteca ```math```, série de Taylor e métodos para determinar as raízes de uma determinada função. Na segunda parte, por sua vez, temos uma apresentação de sistemas lineares, MMQ & Interpolação - nessa parte é bastante utilizada a biblioteca ```numpy```. Na terçeira parte, é visto o conteúdo referente às equações diferenciais.
Todos os métodos serão vistos nesse diretório e, além disso, os trabalhos que podem ser realizados para obtenção da nota terão seus códigos exemplificados também.

## Primeira Parte
<img style="-webkit-user-select: none;margin: auto;cursor: zoom-in;" src="https://raw.githubusercontent.com/leonardoSaaads/ECT_CN/main/imagens/bissec%C3%A7%C3%A3o.png" width="428" height="319">

### Como utilizar - TRABALHO(Calculadora):
Foi definido a classe Calculadora no código em Python - link disponível acima. Para utiliza-la, copie o código e faça a chamada de alguma função ou variável contida na classe no mesmo arquivo copiado (É importante que seja no mesmo arquivo pois assim o python idenficará a propriedade `__name__ == "__main__"`).
Exemplo:
```
class Calculadora:...


if __name__ == "__main__":
  print(Calculadora.somatorio(20, 30, 45, 50, 90))
  print(Calculadora.fatorial(13))
```

Você também pode importar esse arquivo e realizar uma chamada. Exemplo:

```
From (Nome do arquivo salvo em python) import *


print(somatorio(20, 30, 45, 50, 90))
print(fatorial(13))
```

### Como utilizar - FUNÇÕES(Taylor, Raízes):
Vários aquirvos foram disponibilizados para serem baixados e Utilizados individualmente.

## Segunda Parte
<img style="-webkit-user-select: none;margin: auto;cursor: zoom-in;" src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/ab/Secretsharing_3-point.svg/800px-Secretsharing_3-point.svg.png" width="428" height="319">
imagem disponível na wikipédia.

### Como utilizar - TRABALHO:

### Como utilizar - FUNÇÕES:

## Terceira Parte
<img style="-webkit-user-select: none;margin: auto;cursor: zoom-in;" src="https://raw.githubusercontent.com/leonardoSaaads/ECT_CN/main/imagens/euler_method.png" width="428" height="319">

### Como utilizar - TRABALHO(Sistema RLC - Circuitos Elétricos):
<img style="-webkit-user-select: none;margin: auto;" src="https://upload.wikimedia.org/wikipedia/commons/4/4e/RLC_series_circuit.png">
Imagem disponível na wikipédia

Note que um circuito RLC pode ser modelado da seguinte maneira:

<img style="-webkit-user-select: none;margin: auto;cursor: zoom-in;" src="https://raw.githubusercontent.com/leonardoSaaads/ECT_CN/main/imagens/trabalho.png" width="650" height="690">

A partir disso, é possível achar uma solução analítica - EDO homogênea, linear e de coeficientes constantes - e também uma solução aproximada - através do métodos de Euler. Clique [aqui](https://github.com/leonardoSaaads/ECT_CN/blob/main/TRABALHOS%20-(Calculadora%2C%20Criptografia%20%26%20Equac.%20Dif)/Trabalhos%20de%20EDO/EDO%20-%20Circuito%20RLC.py) para acessar o código desse trabalho.
### Como utilizar - TRABALHO(Oscilador Harmônico Amortecido - Leis de Newton):
<img style="-webkit-user-select: none;margin: auto;cursor: zoom-in;" src="https://i.stack.imgur.com/40aXo.png" width="650" height="310">

Note que o oscilador pode ser modelado da seguinte maneira:

<img style="-webkit-user-select: none;margin: auto;cursor: zoom-in;" src="https://raw.githubusercontent.com/leonardoSaaads/ECT_CN/main/imagens/trabalho2.png" width="650" height="330">

A partir disso, é possível achar uma solução analítica - EDO homogênea, linear e de coeficientes constantes - e também uma solução aproximada - através do métodos de Euler. Clique [aqui]() para acessar o código desse trabalho.
### Como utilizar - FUNÇÕES:
