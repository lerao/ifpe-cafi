# Explicação: Gerador de Tabuada

Este projeto é fundamental para entender como automatizar tarefas repetitivas usando computadores.

## Conceitos de JavaScript utilizados:

1.  **Laço de Repetição `for`**: Usado para executar o mesmo bloco de código várias vezes. No nosso caso, ele roda 10 vezes para calcular de 1 a 10.
    -   `let i = 1`: Valor inicial.
    -   `i <= 10`: Condição de parada.
    -   `i++`: Incremento (adiciona 1 a cada volta).
2.  **Operador de Atribuição com Adição (`+=`)**: Usamos `listaTabuada.innerHTML += ...` para adicionar novos itens ao final do conteúdo já existente na lista, sem apagar o anterior.
3.  **Interpolação de Strings**: Facilita a leitura do código ao misturar texto fixo com variáveis: `${num} x ${i} = ${resultado}`.
4.  **Listas do Bootstrap**: Usamos `list-group` e `list-group-item` para criar uma tabela de resultados visualmente organizada e limpa.
