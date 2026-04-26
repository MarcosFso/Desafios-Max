import sys
import os
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from utils.matrizes import (
    criar_matriz_aleatoria,
    somar_matrizes,
    medias_por_linha,
    calcular_determinante,
    transpor_e_multiplicar,
)


class TestCriarMatrizAleatoria:

    def test_dimensoes_corretas(self):
        matriz = criar_matriz_aleatoria(3, 3)
        assert len(matriz) == 3
        for linha in matriz:
            assert len(linha) == 3

    def test_valores_dentro_do_intervalo(self):
        matriz = criar_matriz_aleatoria(4, 4)
        for linha in matriz:
            for valor in linha:
                assert 1 <= valor <= 100

    def test_dimensoes_diferentes(self):
        matriz = criar_matriz_aleatoria(2, 5)
        assert len(matriz) == 2
        assert len(matriz[0]) == 5


class TestSomarMatrizes:

    def test_soma_basica(self):
        A = [[1, 2], [3, 4]]
        B = [[5, 6], [7, 8]]
        assert somar_matrizes(A, B) == [[6, 8], [10, 12]]

    def test_soma_com_zeros(self):
        A = [[1, 2], [3, 4]]
        zeros = [[0, 0], [0, 0]]
        assert somar_matrizes(A, zeros) == A

    def test_soma_negativos(self):
        A = [[-1, -2], [-3, -4]]
        B = [[1, 2], [3, 4]]
        assert somar_matrizes(A, B) == [[0, 0], [0, 0]]


class TestMediasPorLinha:

    def test_media_simples(self):
        matriz = [[1, 2, 3], [4, 5, 6]]
        medias = medias_por_linha(matriz)
        assert medias[0] == pytest.approx(2.0)
        assert medias[1] == pytest.approx(5.0)

    def test_quantidade_de_medias(self):
        matriz = [[10, 20], [30, 40], [50, 60]]
        assert len(medias_por_linha(matriz)) == 3

    def test_media_valores_iguais(self):
        matriz = [[7, 7, 7], [3, 3, 3]]
        medias = medias_por_linha(matriz)
        assert medias[0] == pytest.approx(7.0)
        assert medias[1] == pytest.approx(3.0)


class TestCalcularDeterminante:

    def test_det_2x2(self):
        assert calcular_determinante([[3, 1], [2, 4]]) == pytest.approx(10.0)

    def test_det_3x3(self):
        B = [[1, 2, 3], [0, 1, 4], [5, 6, 0]]
        assert calcular_determinante(B) == pytest.approx(1.0, abs=1e-9)

    def test_matriz_singular(self):
        assert calcular_determinante([[1, 2], [2, 4]]) == pytest.approx(0.0, abs=1e-9)

    def test_matriz_nao_quadrada_lanca_erro(self):
        with pytest.raises(ValueError):
            calcular_determinante([[1, 2, 3], [4, 5, 6]])


class TestTransporEMultiplicar:

    def test_resultado_correto(self):
        estoque = [[1, 0], [0, 1]]
        precos = [[2], [3]]
        resultado = transpor_e_multiplicar(estoque, precos)
        assert resultado[0][0] == pytest.approx(2.0)
        assert resultado[1][0] == pytest.approx(3.0)

    def test_dimensoes_resultado(self):
        estoque = [[10, 20], [5, 15]]
        precos = [[2.0], [3.0]]
        resultado = transpor_e_multiplicar(estoque, precos)
        assert len(resultado) == 2
        assert len(resultado[0]) == 1