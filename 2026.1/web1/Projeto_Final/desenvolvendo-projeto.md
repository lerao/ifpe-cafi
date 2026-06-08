# Guia para auxiliar no projeto

Oi pessoal, algumas pessoas procuraram precisando de ajuda e vou disponibilizar esse guia de como sair do "zero" até ter seu projeto pronto e rodando. 

## Passo 0: Definição do tema

Escolha o projeto que gostaria de construir do zero, seja um tema que você tenha afinidade, App de Clima, Biblioteca de Livros ou o Pomodoro, escolha algo que seja relevante e útil para você!2

Pense antes de começar a implementar, use caderno/papel e desenhe como gostaria de deixar o seu site/app (use wireframes por exemplo, se quiser ler um pouco: https://miro.com/pt/wireframe/o-que-e-wireframe/).

## Passo 1: Estrutura de Pastas
Antes de escrever qualquer código, vc precisa organizar sua  estrutura de pastas. No seu computador, crie a pasta do projeto e dentro dela crie as seguintes subpastas:
- `/css` (para guardar os estilos css - você pode referenciar o bootstrap online e guardar só um style.css com possíveis alterações)
- `/js` (para guardar seus arquivos javascript que vão promover a inteligência do site)
- `/assets` (para imagens, ícones ou fontes)

Crie também seus arquivo principal no lugare correto: `index.html` (na raiz). 
Se desejar, também crie seu arquivo de estilo `css/style.css` e seu arquivo javascript `js/script.js`.


## Passo 2: HTML5 Semântico com Bootstrap

Agora, vamos a prática! Em vez de usar apenas html genéricos como as `<div>` para desenhar o site inteiro, use tags semânticas. Isso significa dar significado verdadeiro ao seu site, o que ajuda na acessibilidade e organização.

Abra seu `index.html` e monte a estrutura básica: 
- Lembre do atalho `!` no vscode para iniciar a estrutura mínima.
- **Inclua o Bootstrap** via CDN na tag `<head>` (procure "Bootstrap CDN" no Google e copie o link do CSS):
  ```html
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
  ```
- **Inclua o seu CSS** também (se tiver criado o arquivo style.css):
  ```html
  <link href="css/style.css" rel="stylesheet">
  ```
- Use `<header>` para o topo do site (onde costuma ir o título ou logotipo).
- Use `<main>` para o conteúdo principal (onde ficará a pesquisa de clima, a lista de tarefas, etc).
- Use `<footer>` para o rodapé da página.
- **Use classes Bootstrap** para estruturar o esqueleto do app/site: coloque `class="container"` nas suas seções, `class="row"` para linhas e `class="col"` para colunas (exemplo: `<div class="container"><div class="row"><div class="col-md-6">...</div></div></div>`).
- *Dica:* Não se esqueça de conectar o seu JavaScript (`<script src="js/script.js" defer></script>`) antes do fechamento da tag `<\body>`. A palavra `defer` avisa ao navegador para carregar o JS só depois de ler todo o HTML. Também adicione o Bootstrap JS no final do `<body>` se precisar de componentes interativos (modals, dropdowns, etc - O Link dele também está na página principal do Bootstrap ou consegues buscando no google).

## Passo 3: CSS e Responsividade com Bootstrap

O **Bootstrap já fornece responsividade automática** e uma super estrutura para gente usar. No entanto, para um *algo a mais* e levar ainda mais modernização ao site/app de vocês, é interessante usar customizações pessoais e aprender que podemos usar "Variáveis CSS" e "Flexbox ou Grid" para o layout, que é como o boostrap trabalha.

### Como usar Bootstrap para estilo:
- **Classes Bootstrap para layout:** Use a grid system do Bootstrap (`container`, `row`, `col-sm-6`, `col-md-4`, etc) para criar layouts responsivos automaticamente. O prefixo `sm`, `md`, `lg` define em qual tamanho de tela aquelas colunas começam (veja a documentação do Bootstrap para mais detalhes).
  ```html
  <div class="container">
    <div class="row">
      <div class="col-md-6">Coluna 1</div>
      <div class="col-md-6">Coluna 2</div>
    </div>
  </div>
  ```
- **Componentes Bootstrap:** Use botões (`btn btn-primary`), cards (`card`), navbars (`navbar`), formulários (`form-control`), etc. Tudo já vem estilizado e responsivo por padrão (veja a documentação do Bootstrap para mais detalhes).
- **Exemplo de botão Bootstrap:**
  ```html
  <button class="btn btn-primary">Buscar</button>
  ```

### Suas customizações pessoais no `style.css`:
"Variáveis CSS" podem ser definidas em seu arquivo `style.css` para personalizar além do Bootstrap:

- **Variáveis CSS:** Defina as cores principais do seu projeto no topo do arquivo:
```css
/* Como definir */
:root {
  --cor-fundo: #f4f4f9;
  --cor-primaria: #007bff;
  --cor-secundaria: #6c757d;
  --cor-texto: #333333;
  --cor-sucesso: #28a745;
}

/* Como referenciar */
body { 
  background-color: var(--cor-fundo); 
  color: var(--cor-texto); 
  font-family: 'Segoe UI', sans-serif;
}
```

- **Flexbox ou Grid:** Se precisar de ajustes finos que o Bootstrap não oferece, combine suas classes CSS com Bootstrap! Fique a vontade! 

- **Dica:** Teste seu site em diferentes tamanhos de tela usando o modo responsivo do navegador (F12 → Device Toolbar no Chrome/Firefox).

## Passo 4: JavaScript Moderno

Aqui devemos usar os exemplos visto em sala, usando *Vanilla JS* (ou seja, JavaScript puro, sem bibliotecas pesadas como React ou jQuery).

**Nota sobre Bootstrap:** O Bootstrap oferece componentes interativos (modals, dropdowns, carrosséis) que já vêm com JavaScript embutido. Seu JavaScript Vanilla vai trabalhar junto para adicionar a lógica específica do seu projeto (buscar dados, salvar informações, filtrar listas).

1. **Variáveis Modernas:** Abandone o `var`. Use sempre `const` para valores que nunca vão mudar (como a referência a um botão do HTML) e `let` para valores que podem mudar (como os minutos de um timer de Pomodoro ou o saldo em Finanças).
2. **Pegar Elementos:** Use `document.querySelector()`,`document.getElementById()`, `document.getElementsByClassName()`, etc., como desejar para selecionar tags, inputs ou botões do seu HTML dentro do JavaScript. Bootstrap usa classes como `btn`, `card`, `modal`, então você pode selecionar por essas classes também:
```javascript
const botaoBuscar = document.querySelector('.btn-primary');
const cards = document.querySelectorAll('.card');
```

3. **Ouvir Eventos:** Como saber que o usuário clicou em buscar? Adicionando um "ouvidor". Exemplo:
```javascript
const botaoBuscar = document.querySelector('#btn-buscar');

botaoBuscar.addEventListener('click', () => {
    console.log('Você clicou no botão!');
    // Aqui vai a lógica de adicionar o livro, ou buscar o clima...
});
```
4. **Listas de Dados:** Para organizar as listas (de tarefas, filmes ou livros), você pode usar arrays. Exemplo (consulte a documentação para entender mais https://blog.talitaoliveira.com.br/como-e-quando-usar-foreach-map-filter-reduce):
   - `.map()`: para transformar dados (ex: pegar uma lista de informações e criar os Cards do Bootstrap no HTML).
   - `.filter()`: para filtrar dados (ex: mostrar apenas os livros com status "Lido").
   - `.forEach()`: para percorrer uma lista e executar uma ação para cada item.

## Passo 5: API ou LocalStorage
Dependendo da opção de projeto que você escolher, você terá uma missão específica:

- **Se escolheu Clima ou Filmes (Consumo de API):**
  Você precisará usar o comando `fetch('url-aqui')`. Pense no Fetch como um garçom: você faz um pedido a ele (ex: "Traga os dados do clima de Recife"), ele vai até a cozinha da internet (a API externa), e volta com as informações (geralmente num formato chamado JSON) para você mostrar na tela. Não esqueça de tratar o tempo de espera (mostrar "Carregando...").

- **Se escolheu Biblioteca, Pomodoro ou Finanças (Uso de LocalStorage):**
  Se o usuário fechar a aba, ele perderá todas as tarefas? Não! Você usará o banco de dados interno do navegador.
  - Para salvar os dados, use: `localStorage.setItem('meusLivros', JSON.stringify(dados))`.
  - Para recuperar os dados ao carregar a página: `JSON.parse(localStorage.getItem('meusLivros'))`.

## Passo 6: O outro lado da ponte

- **Resiliência:** O que acontece se o usuário buscar uma cidade que não existe? Ou clicar para adicionar um livro com o título vazio? Então, tente tratar esses erros exibindo alertas amigáveis na tela em vez de quebrar o site.

- **Documentação:** Crie um arquivo `README.md` simples contendo o nome do seu projeto, as tecnologias usadas e como rodá-lo (ex: "Basta abrir o arquivo index.html em seu navegador preferido").

Pronto! Siga essa trilha passo a passo, foque em resolver um problema de cada vez, e você conseguirá desenvolver um excelente projeto!
