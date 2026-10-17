def calcular_frete(valor_carrinho, regiao=None, expresso=False, **kwargs):
    if "frete_expresso" in kwargs:
        expresso = kwargs["frete_expresso"]

    if valor_carrinho >= 250:
        frete = 0.0
    else:
        frete = 15.0

    if expresso:
        frete += 10.0

    return frete

def calcular_total_com_frete(valor_carrinho, expresso=False, **kwargs):
    frete = calcular_frete(valor_carrinho, expresso=expresso, **kwargs)
    return valor_carrinho + frete

if __name__ == "__main__":
    import sys

    valor = float(sys.argv[1])
    expresso = len(sys.argv) > 2 and sys.argv[2].lower() in ("--expresso", "expresso", "true", "1")
    frete = calcular_frete(valor, expresso=expresso)

    print(frete)

class ServicoFrete:
    def __init__(self, servico_logistica, servico_notificacao):
        self.servico_logistica = servico_logistica
        self.servico_notificacao = servico_notificacao

    def confirmar_frete(self, pedido_id, usuario):
        taxa = self.servico_logistica.consultar_taxa(pedido_id)

        self.servico_notificacao.enviar_notificacao_rastreio(pedido_id)

        return taxa