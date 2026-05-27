# Documento de Requisitos: Projetos Práticos de Desenvolvimento Web

Este documento detalha os requisitos para sugestões de projetos práticos. Deve ser escolhido **apenas um** para implementar. O objetivo é aplicar conhecimentos de HTML5, CSS3 e JavaScript Moderno (ES6+). Faz parte do projeto a busca ativa por conhecimentos extras para conseguir resolver todo o projeto.

---

## 1. Requisitos Gerais (Para todos os projetos)

### Técnicos
*   **HTML5:** Uso de tags semânticas (`<header>`, `<main>`, `<footer>`, `<section>`, etc.).
*   **CSS3:** Layout responsivo (Flexbox ou Grid), variáveis CSS para cores e fontes, e boa legibilidade.
*   **JavaScript:** Manipulação do DOM sem bibliotecas externas (Vanilla JS), uso de `const`/`let`, `arrow functions` e métodos de array (`map`, `filter`, `forEach`).
*   **Responsividade:** A aplicação deve funcionar bem em dispositivos móveis e desktops.

### Entrega
*   Código fonte organizado em pastas (`/css`, `/js`, `/assets`).
*   README simples explicando como rodar o projeto.

---

## 2. Requisitos Específicos por Projeto

### Opção A: Dashboard de Clima (Weather App)
**Objetivo:** Criar uma aplicação que mostre dados climáticos em tempo real.

*   **RF01:** Permitir a busca do clima por nome da cidade (usando OpenWeatherMap API ou similar).
*   **RF02:** Exibir temperatura atual, umidade, velocidade do vento e uma descrição (ex: "Céu Limpo").
*   **RF03:** Alterar dinamicamente a imagem de fundo ou ícones baseados na condição climática (Sol, Chuva, Neve).
*   **RF04:** Exibir a data e hora local da consulta formatada.
*   **Diferencial:** Usar a API de Geolocalização do navegador para carregar o clima da cidade atual automaticamente.

### Opção B: Inventário de Livros (My Library)
**Objetivo:** Um sistema de gerenciamento de coleção pessoal.

*   **RF01:** Cadastro de livros (Título, Autor, Categoria e Status: "Lido" ou "Lendo").
*   **RF02:** Sistema de filtros por Categoria ou Status.
*   **RF03:** Opção de editar o status de um livro já cadastrado.
*   **RF04:** Armazenar a biblioteca no `localStorage`.
*   **Diferencial:** Adicionar uma barra de progresso que mostre a porcentagem de livros lidos em relação ao total.

### Opção C: App de Foco (Pomodoro + Tasks)
**Objetivo:** Ferramenta de produtividade com timer e lista de tarefas.

*   **RF01:** Timer de contagem regressiva (25 min para foco, 5 min para pausa).
*   **RF02:** Botões de Iniciar, Pausar e Resetar o timer.
*   **RF03:** Lista de tarefas simples (To-Do) abaixo do timer para o usuário anotar o que está fazendo.
*   **RF04:** Emitir um alerta visual (notificação ou mudança de cor) quando o tempo acabar.
*   **Diferencial:** Tocar um som discreto ao final do ciclo de foco.

---

## 3. Critérios de Avaliação
1.  **Funcionalidade:** Todos os requisitos obrigatórios (RF) foram atendidos?
2.  **Qualidade do Código:** O código está limpo, indentado e bem comendado?
3.  **Interface (UI):** A aplicação é agradável e fácil de usar?
4.  **Resiliência:** Trata erros (ex: busca de cidade inexistente ou campo vazio)?


## 4. Exemplos de Entrega

### Exemplo 1: Gerenciador de Finanças (Fintech)
**Objetivo:** Criar um dashboard para controle de gastos e ganhos.

*   **RF01:** Permitir a entrada de transações (Nome, Valor e Tipo: Receita ou Despesa).
*   **RF02:** Exibir o saldo atualizado (Total de Receitas - Total de Despesas).
*   **RF03:** Listar todas as transações cadastradas com opção de excluir.
*   **RF04:** Persistir os dados no `localStorage` para que não sejam perdidos ao recarregar a página.
*   **Diferencial:** Exibir um gráfico simples de barras ou cores diferentes para valores positivos/negativos.

### Exemplo 2: Catálogo de Filmes (API Explorer)
**Objetivo:** Consumir dados de uma API externa e exibi-los dinamicamente.

*   **RF01:** Integrar com a API do TMDB (ou similar) para buscar filmes.
*   **RF02:** Criar uma barra de busca que filtre os filmes por nome em tempo real ou ao clicar no botão.
*   **RF03:** Exibir cards com imagem do poster, título e nota (rating).
*   **RF04:** Implementar um estado de "Carregando..." enquanto os dados são buscados.
*   **Diferencial:** Permitir que o usuário clique no filme para ver uma sinopse em um modal.