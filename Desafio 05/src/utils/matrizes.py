import numpy as np
import random


def criar_matriz_aleatoria(linhas: int, colunas: int) -> list:
    matriz = [[0] * colunas for _ in range(linhas)]
    for i in range(linhas):
        for j in range(colunas):
            matriz[i][j] = random.randint(1, 100)
    return matriz


def somar_matrizes(A: list, B: list) -> list:
    linhas = len(A)
    colunas = len(A[0])
    resultado = [[0] * colunas for _ in range(linhas)]
    for i in range(linhas):
        for j in range(colunas):
            resultado[i][j] = A[i][j] + B[i][j]
    return resultado


def medias_por_linha(matriz: list) -> list:
    np_matriz = np.array(matriz)
    medias = np_matriz.mean(axis=1)
    return medias.tolist()


def calcular_determinante(matriz: list) -> float:
    np_matriz = np.array(matriz, dtype=float)
    if np_matriz.shape[0] != np_matriz.shape[1]:
        raise ValueError("A matriz precisa ser quadrada para calcular o determinante.")
    return float(np.linalg.det(np_matriz))


def transpor_e_multiplicar(estoque: list, precos: list) -> list:
    np_estoque = np.array(estoque, dtype=float)
    np_precos = np.array(precos, dtype=float)
    transposta = np_estoque.T
    resultado = np.dot(transposta, np_precos)
    return resultado.tolist()