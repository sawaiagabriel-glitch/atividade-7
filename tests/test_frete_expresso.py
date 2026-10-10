from src.frete import calcular_frete, calcular_total_com_frete


def test_frete_expresso_abaixo_250():
    """Carrinho < R$ 250 com frete expresso deve cobrar R$ 15,00 (padrão) + R$ 10,00 (expresso) = R$ 25,00."""
    assert calcular_frete(200.0, expresso=True) == 25.0
    assert calcular_frete(150.0, expresso=True) == 25.0


def test_frete_expresso_acima_ou_igual_250():
    """Carrinho >= R$ 250 com frete expresso deve cobrar R$ 0,00 (grátis) + R$ 10,00 (expresso) = R$ 10,00."""
    assert calcular_frete(250.0, expresso=True) == 10.0
    assert calcular_frete(300.0, expresso=True) == 10.0


def test_total_com_frete_expresso():
    """Totalizador com frete expresso deve somar a taxa expressa ao subtotal."""
    assert calcular_total_com_frete(200.0, expresso=True) == 225.0
    assert calcular_total_com_frete(250.0, expresso=True) == 260.0
