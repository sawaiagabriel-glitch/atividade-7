ef calcular_frete(valor_carrinho, regiao=None):
    if valor_carrinho >= 250:
        return 0.0

    return 15.0

def calcular_total_com_frete(valor_carrinho):
    frete = calcular_frete(valor_carrinho)
    return valor_carrinho + frete

if __name__ == "__main__":
    import sys

    valor = float(sys.argv[1])
    frete = calcular_frete(valor)

    print(frete)