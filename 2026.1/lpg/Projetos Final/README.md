# Projeto final da disciplina de Lógica de Programação.

## Requisitos a serem avaliados
- Entrada e Saída de Dados 
- Estruturas de Decisão 
- Laços de Repetição 
- Funções e Escopo
- Estruturas de Dados
- Manipulação de Arquivos 
- Orientação a Objetos

## Projetos Disponíveis
1.  **Pizzaria:** Foco em menus, IDs únicos e cálculo de vendas.
2.  **Biblioteca:** Foco em status de objetos (disponível/emprestado) e busca por ID.
3.  **Controle de Estoque:** Foco em atualização de quantidades e validação de estoque.
4.  **Sistema Escolar:** Foco em processamento de dados (médias) e condicional de aprovação.

## O Gerenciador de Arquivos (`gerenciador_arquivos.py`)
Todos os projetos devem utilizar a classe `GerenciadorArquivo`. Ela é responsável por transformar suas listas de dados em arquivos CSV e vice-versa.
O diferencial é a **conversão automática de tipos**: ao ler um arquivo, ela tenta transformar o texto em número (`int` ou `float`) automaticamente, permitindo que você faça cálculos matemáticos sem precisar de `int()` ou `float()` toda vez que ler do arquivo.

### Como rodar?
1. Crie seu projeto e copie o arquivo `gerenciador_arquivos.py` para a pasta do seu projeto.
2. Em seu arquivo `main.py`, importe a classe `GerenciadorArquivo`.
3. Crie uma instância do GerenciadorArquivo ex: `db = GerenciadorArquivo("seu_banco_de_dados.csv")`
4. Para ler dados  de seu banco de dados, chame o método `ler_dados()`.
5. Para salvar dados no seu banco de dados, chame o método `salvar_dados()`.

---
Bons estudos e boa prática!