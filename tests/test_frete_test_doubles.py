from unittest.mock import Mock

from src.frete import ServicoFrete


def test_confirmar_frete_com_test_doubles():
    # Arrange

    # Dummy: apenas satisfaz a assinatura, não participa da lógica
    dummy_usuario = object()

    # Stub: retorna uma taxa fixa sem acessar rede
    stub_logistica = Mock()
    stub_logistica.consultar_taxa.return_value = 15.0

    # Mock / Spy: registra chamadas para posterior verificação
    mock_notificacao = Mock()

    pedido_id = 123

    servico_frete = ServicoFrete(
        servico_logistica=stub_logistica,
        servico_notificacao=mock_notificacao
    )

    # Act
    taxa = servico_frete.confirmar_frete(
        pedido_id=pedido_id,
        usuario=dummy_usuario
    )

    # Assert
    assert taxa == 15.0

    stub_logistica.consultar_taxa.assert_called_once_with(pedido_id)

    mock_notificacao.enviar_notificacao_rastreio.assert_called_once_with(
        pedido_id
    )