# Explicação: Calculadora de Média

Este projeto é o ponto de partida para entender como o JavaScript interage com o HTML (DOM) e realiza cálculos simples.

## Conceitos de JavaScript utilizados:

1.  **`document.getElementById()`**: Usado para "pegar" um elemento do HTML pelo seu ID e trazê-lo para o JavaScript.
2.  **`const` e `let`**: 
    -   `const` para valores que não mudam (referências a elementos do HTML).
    -   `let` para valores que podem ser alterados (como a situação do aluno).
3.  **`Number()`**: Converte o texto digitado no campo de input (que sempre vem como String) em um número real para podermos fazer contas.
4.  **Operadores Matemáticos**: Usamos `+` para somar e `/` para dividir.
5.  **`if...else` (Condicionais)**: Permite que o programa tome decisões. Se a média for 7 ou mais, acontece uma coisa; caso contrário, acontece outra.
6.  **`addEventListener('click', ...)`**: "Escuta" quando o usuário clica no botão para disparar a função de cálculo.
7.  **`innerHTML`**: Permite alterar o conteúdo de um elemento HTML e até inserir novas tags (como o `<span>` para mudar a cor).
8.  **`toFixed(1)`**: Formata o número para exibir apenas uma casa decimal.
