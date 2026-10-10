# Roteiro de Testes — Cálculo de Frete

> **Nota de Contexto:** O projeto é composto exclusivamente pelo módulo [`src/frete.py`](file:///C:/Users/Gabriel/Documents/GitHub/atividade%206/src/frete.py), sem interface gráfica, telas ou banco de dados. Os testes abaixo refletem a realidade do código e propõem a menor extensão necessária para viabilizar testes de múltiplos níveis.

---

## 1. Teste Unitário

### CT-UNIT-01 — Cálculo de frete padrão (valor abaixo de R$ 250,00)

**Objetivo:**  
Verificar se a função [`calcular_frete`](file:///C:/Users/Gabriel/Documents/GitHub/atividade%206/src/frete.py#L1-L5) retorna o valor fixo de R$ 15,00 para carrinhos com valor inferior a R$ 250,00.

**Pré-condição:**  
O módulo [`src/frete.py`](file:///C:/Users/Gabriel/Documents/GitHub/atividade%206/src/frete.py) deve estar disponível para importação.

**Procedimento:**
1. Chamar a função `calcular_frete(150.0)`.
2. Chamar a função `calcular_frete(200.0)`.
3. Chamar a função `calcular_frete(249.99)` (valor limite).
4. Verificar o retorno de cada chamada.

**Resultado esperado:**  
A função deve retornar `15.0` para todas as chamadas.

**Tipo:** Teste Unitário.

---

### CT-UNIT-02 — Concessão de frete grátis (valor igual ou superior a R$ 250,00)

**Objetivo:**  
Verificar se a função [`calcular_frete`](file:///C:/Users/Gabriel/Documents/GitHub/atividade%206/src/frete.py#L1-L5) retorna `0.0` (frete grátis) quando o subtotal do carrinho for maior ou igual a R$ 250,00.

**Pré-condição:**  
O módulo [`src/frete.py`](file:///C:/Users/Gabriel/Documents/GitHub/atividade%206/src/frete.py) deve estar disponível para importação.

**Procedimento:**
1. Chamar a função `calcular_frete(250.0)` (valor limite exato).
2. Chamar a função `calcular_frete(300.0)`.
3. Verificar o retorno de cada chamada.

**Resultado esperado:**  
A função deve retornar `0.0` para todas as chamadas.

**Tipo:** Teste Unitário.

---

## 2. Teste de Integração

> **Funcionalidade Proposta (a ser implementada futuramente):**  
> Para permitir um teste de integração real no escopo do projeto, propõe-se a função auxiliar `calcular_total_com_frete(valor_carrinho)` (ou `calcular_total_pedido`), que orquestra a chamada a [`calcular_frete`](file:///C:/Users/Gabriel/Documents/GitHub/atividade%206/src/frete.py#L1-L5) e soma o frete ao subtotal, atendendo ao requisito REQ-01 ("calcular o valor total adicionando a taxa de frete ao subtotal").

### CT-INT-01 — Integração entre totalizador de pedido e cálculo de frete

**Objetivo:**  
Verificar se a função totalizadora `calcular_total_com_frete` se integra corretamente à função [`calcular_frete`](file:///C:/Users/Gabriel/Documents/GitHub/atividade%206/src/frete.py#L1-L5), compondo o valor final da compra somando o subtotal à taxa calculada.

**Pré-condição:**  
A função `calcular_total_com_frete` deve estar implementada e integrada com `calcular_frete`.

**Procedimento:**
1. Executar `calcular_total_com_frete(valor_carrinho=200.0)`.
2. A função totalizadora deve invocar internamente `calcular_frete(200.0)`.
3. Verificar se o resultado retornado equivale a `200.0 + 15.0`.
4. Executar `calcular_total_com_frete(valor_carrinho=250.0)`.
5. A função totalizadora deve invocar internamente `calcular_frete(250.0)`.
6. Verificar se o resultado retornado equivale a `250.0 + 0.0`.

**Resultado esperado:**  
- Para o valor de R$ 200,00, a saída integrada deve ser `215.0`.
- Para o valor de R$ 250,00, a saída integrada deve ser `250.0`.

**Tipo:** Teste de Integração.

---

## 3. Teste Funcional

### CT-FUNC-01 — Execução do fluxo de cálculo de frete via interface de linha de comando (CLI)

**Objetivo:**  
Validar o fluxo completo de consulta de frete da perspectiva do usuário final via terminal (execução como script/CLI com passagem de parâmetros ou entrada padrão), sem dependência de interface gráfica ou web.

**Pré-condição:**  
O script [`src/frete.py`](file:///C:/Users/Gabriel/Documents/GitHub/atividade%206/src/frete.py) deve possuir um bloco de execução principal (`if __name__ == '__main__':`) que receba o valor do carrinho via argumento de linha de comando ou `input()` e imprima o valor do frete na saída padrão (`stdout`).

**Procedimento:**
1. Executar o script no terminal passando o valor `200.0` (exemplo: `python -m src.frete 200.0`).
2. Capturar a saída gerada no console (`stdout`).
3. Executar novamente o script no terminal passando o valor `250.0` (exemplo: `python -m src.frete 250.0`).
4. Capturar a saída gerada no console (`stdout`).

**Resultado esperado:**  
- Na primeira execução (R$ 200,00), o sistema deve exibir no terminal a cobrança do frete de `15.0` (ou mensagem informativa correspondente).
- Na segunda execução (R$ 250,00), o sistema deve exibir no terminal a concessão de frete grátis `0.0`.

**Tipo:** Teste Funcional.
