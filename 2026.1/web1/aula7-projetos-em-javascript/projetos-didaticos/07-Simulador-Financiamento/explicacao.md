# Explicação: Simulador de Financiamento

Este projeto combina vários campos de entrada para gerar um relatório de cálculo financeiro.

## Conceitos de JavaScript utilizados:

1.  **Lógica de Negócio**: Separamos o valor que o usuário já tem (entrada) do valor que ele realmente vai pegar emprestado (financiado).
2.  **Operações Matemáticas de Financiamento**: Aplicamos uma fórmula de juros simples para demonstrar como cálculos de tempo e taxa funcionam programaticamente.
3.  **Manipulação de Classes CSS (`classList`)**: Usamos `divResultado.classList.remove('d-none')` para esconder o resultado até que o botão seja clicado. A classe `d-none` do Bootstrap significa "display: none".
4.  **Layout Responsivo com Grid**: No HTML, usamos as classes `row` e `col-md-6` para que os campos fiquem lado a lado em telas grandes e um sobre o outro em celulares.
5.  **Interação entre Múltiplos Inputs**: Demonstramos como o JS pode processar 4 fontes de dados diferentes ao mesmo tempo para chegar a um único resultado.
