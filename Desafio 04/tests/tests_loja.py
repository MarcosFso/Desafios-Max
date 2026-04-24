import pytest
from src.utils.loja import *


def test_criar_produto():
    p = criar_produto("Camiseta", 50, 10)
    assert p["nome"] == "Camiseta"


def test_produto_invalido():
    with pytest.raises(ValueError):
        criar_produto("", 10, 5)


def test_adicionar_produto():
    produtos = []
    p = criar_produto("Camiseta", 50, 10)
    adicionar_produto(produtos, p)
    assert len(produtos) == 1


def test_calcular_venda():
    produto = {"nome": "Camiseta", "preco": 50, "estoque": 20}
    venda = calcular_venda(produto, 2)
    assert venda["valor_final"] == 100


def test_desconto():
    produto = {"nome": "Camiseta", "preco": 50, "estoque": 20}
    venda = calcular_venda(produto, 15)
    assert venda["desconto"] == 37.5


def test_total():
    vendas = [
        {"valor_final": 100},
        {"valor_final": 200}
    ]
    assert total_arrecadado(vendas) == 300


def test_estoque_atualizado():
    produto = {"nome": "Camiseta", "preco": 50, "estoque": 20}
    calcular_venda(produto, 5)
    assert produto["estoque"] == 15