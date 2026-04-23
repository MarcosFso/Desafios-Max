from src.calculos import calcular_clt


def test_clt():
    liquido, inss, irrf = calcular_clt(3000)
    assert inss == 240
    assert irrf == 300