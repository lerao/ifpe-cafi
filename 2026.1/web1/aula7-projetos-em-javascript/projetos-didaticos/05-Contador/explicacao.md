# Explicação: Contador Digital

Este projeto introduz a ideia de um "estado" global que persiste enquanto o usuário interage com a página.

## Conceitos de JavaScript utilizados:

1.  **Escopo Global (`let contador`)**: A variável `contador` é criada fora de qualquer função, permitindo que todas as funções (aumentar, diminuir, resetar) consigam acessá-la e modificá-la.
2.  **`textContent`**: Usado para alterar apenas o texto de um elemento, sendo mais seguro que o `innerHTML` quando não precisamos inserir tags HTML.
3.  **Manipulação de Estilo Direto (`style.color`)**: Mostramos como o JavaScript pode alterar propriedades de CSS em tempo real para dar feedback visual.
4.  **Múltiplos Event Listeners**: Um único projeto com três botões diferentes, cada um executando sua própria função.
5.  **Refatoração Simples (`atualizarTela`)**: Criamos uma função separada apenas para cuidar da parte visual, que é chamada por todas as outras funções de ação. Isso evita repetição de código (Princípio DRY - *Don't Repeat Yourself*).
