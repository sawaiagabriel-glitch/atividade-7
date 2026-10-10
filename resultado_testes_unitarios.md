# Exercício 6.2 — Teste Unitário

Foram executados testes unitários sobre a função `calcular_frete`.

Casos testados:
- valores abaixo de R$ 250,00 retornam frete de R$ 15,00;
- valores iguais ou superiores a R$ 250,00 retornam frete grátis.

Comando utilizado:

python -m pytest

Resultado:

2 testes executados com sucesso.

Status: APROVADO



# Exercício 6.3 — Teste de Integração

Comando executado:
python -m pytest tests/test_integracao_frete.py

Casos executados:
- integração entre calcular_total_com_frete e calcular_frete para subtotal de R$ 200,00
- integração entre calcular_total_com_frete e calcular_frete para subtotal de R$ 250,00

Resultado esperado:
- R$ 200,00 + R$ 15,00 = R$ 215,00
- R$ 250,00 + R$ 0,00 = R$ 250,00

Resultado obtido:
[preencher com o resultado real do pytest]

Status:
[APROVADO ou REPROVADO]

Exercício 6.4 — Teste Funcional

Fluxo testado:
Execução do cálculo de frete pela interface de linha de comando.

Casos:
- valor do carrinho = R$ 200,00 → frete = R$ 15,00
- valor do carrinho = R$ 250,00 → frete = R$ 0,00

Comando executado:
python -m pytest tests/test_funcional_frete.py

Resultado:
[preencher com o resultado real]

Status:
[APROVADO ou REPROVADO]