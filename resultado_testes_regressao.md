# Exercício 6.5 — Testes de Regressão

## 1. Nova Funcionalidade Implementada
- **Frete Expresso**: Implementação do parâmetro `expresso=False` na função `calcular_frete` (e em `calcular_total_com_frete`), permitindo a contratação de frete expresso.
- **Regras aplicadas**:
  - Quando `expresso=False` (padrão): o comportamento permanece rigorosamente inalterado (R$ 15,00 para carrinhos < R$ 250,00; R$ 0,00 para carrinhos >= R$ 250,00).
  - Quando `expresso=True`: adiciona-se uma taxa fixa de R$ 10,00 ao valor do frete calculado (ex.: R$ 200,00 -> R$ 25,00; R$ 250,00 -> R$ 10,00).

## 2. Testes Novos Criados
Arquivo: `tests/test_frete_expresso.py`
- `test_frete_expresso_abaixo_250`: valida que carrinhos com valor abaixo de R$ 250,00 com frete expresso retornam R$ 25,00.
- `test_frete_expresso_acima_ou_igual_250`: valida que carrinhos com valor igual ou superior a R$ 250,00 com frete expresso retornam R$ 10,00.
- `test_total_com_frete_expresso`: valida que o totalizador `calcular_total_com_frete` calcula corretamente o valor total com frete expresso.

## 3. Resultados dos Testes de Regressão
- **Comando executado**: `python -m pytest`
- **Quantidade total de testes executados**: 9
- **Quantidade de testes antigos que continuaram passando**: 6
  - `tests/test_frete.py`: 2 testes unitários aprovados
  - `tests/test_funcional_frete.py`: 2 testes funcionais aprovados
  - `tests/test_integracao_frete.py`: 2 testes de integração aprovados
- **Quantidade de testes novos que passaram**: 3
- **Falhas**: 0
- **Status final da regressão**: APROVADO
