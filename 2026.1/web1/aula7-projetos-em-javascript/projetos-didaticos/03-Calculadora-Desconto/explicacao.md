# Explicação: Calculadora de Desconto

Este projeto foca na aplicação prática de cálculos matemáticos que usamos no dia a dia.

## Conceitos de JavaScript utilizados:

1.  **Cálculo de Porcentagem**: Para calcular X% de um valor, multiplicamos o valor por (X/100).
2.  **Operadores de Atribuição e Subtração**: Calculamos o desconto e depois subtraímos do valor original.
3.  **Formatação de Moeda**: Usamos `toFixed(2)` para garantir que o preço sempre exiba dois dígitos após a vírgula (centavos). 
    -   *Dica Extra*: Em projetos reais, poderíamos usar `valor.toLocaleString('pt-br', {style: 'currency', currency: 'BRL'})` para uma formatação ainda mais profissional.
4.  **Estrutura de Cards do Bootstrap**: Utilizamos as classes `card`, `card-header`, `card-body` e `card-footer` para organizar visualmente as informações.
