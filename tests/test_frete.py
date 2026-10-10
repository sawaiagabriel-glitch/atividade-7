from src.frete import calcular_frete


def test_frete_padrao():
    """CT-UNIT-01: Cálculo de frete padrão para valores abaixo de R$ 250,00."""
    assert calcular_frete(150) == 15.0
    assert calcular_frete(200) == 15.0
    assert calcular_frete(249.99) == 15.0


def test_frete_gratis():
    """CT-UNIT-02: Concessão de frete grátis para valores iguais ou superiores a R$ 250,00."""
    assert calcular_frete(250) == 0.0
    assert calcular_frete(300) == 0.0

