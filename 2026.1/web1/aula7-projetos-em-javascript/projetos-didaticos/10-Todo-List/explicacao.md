# Explicação: Lista de Tarefas (Todo-List)

Este é o projeto mais completo, pois envolve a manipulação total do ciclo de vida de um elemento (criação, modificação e remoção).

## Conceitos de JavaScript utilizados:

1.  **`document.createElement()`**: Diferente dos projetos anteriores onde apenas mudávamos textos ou imagens, aqui criamos "do nada" novos elementos HTML.
2.  **`appendChild()`**: Adiciona o elemento recém-criado como um "filho" de outro elemento (colocamos o `<li>` dentro do `<ul>`).
3.  **`removeChild()`**: Remove um elemento da página. Usamos para deletar uma tarefa da lista.
4.  **`trim()`**: Remove espaços em branco desnecessários no início e no fim do texto digitado pelo usuário.
5.  **`classList.toggle()`**: Uma forma elegante de adicionar ou remover uma classe CSS. Se a classe já existir, ela sai; se não existir, ela entra. Usamos para riscar a tarefa concluída.
6.  **`event.key`**: Verificamos qual tecla foi pressionada. Isso permite que o usuário adicione tarefas apenas apertando "Enter", sem precisar clicar no botão.
7.  **Escopo de Evento Local**: Mostramos como adicionar ouvintes de evento (`addEventListener`) individualmente em cada tarefa assim que ela é criada.
