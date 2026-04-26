import random
import numpy as np


def metodo_random():
    # Inicializa uma lista vazia para a matriz
    matriz = []

    num_linhas = 3
    num_colunas = 3

    # Define o intervalo para os números aleatórios (ex: de 0 a 9)
    min_valor = 0
    max_valor = 9

    for i in range(num_linhas):
        # Cria uma nova linha (lista) para cada iteração
        linha = []

        for j in range(num_colunas):
            # Gera um número inteiro aleatório e o adiciona à linha
            numero_aleatorio = random.randint(min_valor, max_valor)
            linha.append(numero_aleatorio)

        # Adiciona a linha completa à matriz
        matriz.append(linha)

    return matriz


def metodo_numpy():
    # Define o intervalo para os números aleatórios (ex: de 0 a 9)
    min_valor = 0
    max_valor = 10  # O valor máximo é exclusivo no randint do NumPy

    # Gera uma matriz 3x3 com números inteiros aleatórios
    matriz = np.random.randint(min_valor, max_valor, size=(3, 3))

    return matriz