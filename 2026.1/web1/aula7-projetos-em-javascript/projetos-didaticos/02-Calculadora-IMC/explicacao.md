# Explicação: Calculadora de IMC

Neste segundo projeto, avançamos um pouco na lógica de programação introduzindo validações e múltiplas condições.

## Conceitos de JavaScript utilizados:

1.  **Operadores Matemáticos Avançados**: Usamos a fórmula `peso / (altura * altura)`. Também poderíamos usar `Math.pow(altura, 2)` ou o operador de exponenciação `**`.
2.  **Validação de Dados (`if` com `return`)**: Verificamos se o usuário digitou valores válidos. O comando `return` dentro de uma função faz com que ela pare de ser executada naquele momento.
3.  **Operadores Lógicos (`||`)**: O símbolo `||` significa "OU". Usamos para verificar se o peso OU a altura estão incorretos.
4.  **Estrutura `else if`**: Diferente do `if/else` simples, o `else if` permite testar várias condições em sequência até encontrar a verdadeira.
5.  **Template Strings (Crases `` ` ``)**: Usamos as crases para criar strings que ocupam várias linhas e facilitam a inclusão de variáveis com `${variavel}`.
6.  **Classes do Bootstrap via JS**: Inserimos uma `div` com a classe `alert alert-info` dinamicamente para melhorar o visual do resultado.
