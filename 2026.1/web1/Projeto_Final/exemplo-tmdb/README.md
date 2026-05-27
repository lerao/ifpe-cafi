# Exemplo 2: Catálogo de Filmes (API Explorer)

Este projeto é um exemplo prático de como consumir dados de uma API externa (The Movie Database - TMDB) e exibi-los dinamicamente em uma página web.

## Como rodar o projeto
1. Abra o arquivo `index.html` diretamente no seu navegador.
2. Certifique-se de estar conectado à internet para que a API possa carregar os dados.

## O que foi utilizado:
- **HTML5:** Tags semânticas como `<header>`, `<main>` e `<dialog>`.
- **CSS3:** Uso de **CSS Grid** para criar a grade de filmes de forma automática e responsiva.
- **JavaScript Moderno:**
  - `fetch` com `async/await` para buscar dados de forma síncrona/sequencial.
  - `map` para percorrer a lista de filmes.
  - `Template Literals` (crases) para injetar HTML diretamente do JavaScript.
  - Manipulação do DOM para exibir o estado de "Carregando" e o Modal.

## Estrutura de Pastas
- `/css`: Contém o estilo visual (`style.css`).
- `/js`: Contém a lógica de programação (`script.js`).
- `index.html`: Arquivo principal do projeto.
