from src.frete import calcular_total_com_frete


def test_total_com_frete_padrao():
    assert calcular_total_com_frete(200.0) == 215.0


def test_total_com_frete_gratis():
    assert calcular_total_com_frete(250.0) == 250.0
