# Explicação: Lâmpada Interativa

Este projeto sai dos números e entra na manipulação visual direta de elementos da página.

## Conceitos de JavaScript utilizados:

1.  **Manipulação do Atributo `src`**: Mostramos como trocar o caminho de uma imagem dinamicamente para alterar o que o usuário vê.
2.  **`indexOf()`**: Usado para procurar uma palavra dentro de um texto. Aqui usamos para checar se o nome do arquivo da imagem contém "quebrada".
3.  **Evento `mouseover` e `mouseleave`**: Permite criar interações que não dependem de cliques, apenas do movimento do ponteiro do mouse.
4.  **Evento `dblclick`**: Reconhece quando o usuário clica rapidamente duas vezes no mesmo elemento.
5.  **Lógica de Proteção**: Usamos a função `estaQuebrada()` dentro das outras funções para garantir que uma lâmpada quebrada não possa ser ligada ou desligada (uma vez quebrada, ela fica assim).
