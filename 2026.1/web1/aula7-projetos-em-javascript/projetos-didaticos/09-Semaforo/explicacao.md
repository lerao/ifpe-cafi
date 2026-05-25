# Explicação: Semáforo Inteligente

Este projeto ensina como fazer o JavaScript "trabalhar sozinho" através de temporizadores.

## Conceitos de JavaScript utilizados:

1.  **Objetos Literais (`const cores = { ... }`)**: Usamos um objeto para mapear nomes de cores para seus respectivos arquivos de imagem, tornando o código mais limpo e organizado.
2.  **`setInterval()`**: Uma função que executa um bloco de código repetidamente em um intervalo de tempo definido (em milissegundos).
3.  **`clearInterval()`**: Interrompe um timer que foi iniciado anteriormente. É essencial para não deixar processos rodando infinitamente em segundo plano.
4.  **Arrays e Índices**: Usamos um array `['vermelho', 'amarelo', 'verde']` e uma variável de controle `indiceCor` para percorrer as cores em sequência.
5.  **Delegação de Eventos**: Em vez de colocar um `addEventListener` em cada botão, colocamos um no "pai" de todos eles e verificamos qual foi clicado através de `event.target.id`.
6.  **Ternário e Incremento**: Usamos `indiceCor < 2 ? ++indiceCor : 0` para fazer o semáforo voltar para o vermelho (0) após chegar no verde (2).
