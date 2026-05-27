# Atividades Práticas: IHC e Acessibilidade Digital

Este guia contém as instruções para as três oficinas práticas de Interação Humano-Computador. O objetivo é aplicar os conceitos de **WCAG**, **Design Emocional** e **Leiturabilidade** em cenários reais de código.

---

## 🛠️ Atividade 1: Acessibilidade Fundamental (WCAG)
**Arquivo:** `7-Oficina1-Acessibilidade-Desafio.html`

**O Desafio:** Você recebeu um protótipo de formulário acadêmico que "parece" bonito, mas é um desastre para tecnologias assistivas.
1. **Navegação por Teclado:** Tente navegar no formulário usando apenas a tecla `TAB`. Onde o foco se perde?
2. **Semântica:** Inspecione o botão de envio. Por que ele não funciona com a tecla `Enter`?
3. **Labels:** Tente clicar no texto "Nome Completo". O cursor deveria ir para o campo de texto automaticamente. Por que não vai?

**Sua missão:** Corrigir o HTML para que a nota de Acessibilidade no **Chrome Lighthouse** chegue a 100.

---

## 📖 Atividade 2: Cirurgia de Leiturabilidade
**Arquivo:** `8-Oficina2-Leiturabilidade-Desafio.html`

**O Desafio:** O texto da Política de Privacidade está "ilegível" devido a péssimas escolhas de design.
1. **Contraste:** Use um verificador de contraste (como o [Adobe Contrast Checker](https://color.adobe.com/pt/create/color-contrast-analyzer)) e veja se o texto passa nos critérios WCAG.
2. **Carga Cognitiva:** O texto ocupa a largura total da tela e não tem respiros. Isso cansa o usuário.
3. **Tipografia:** A fonte serifada minúscula dificulta o rastreamento visual.

**Sua missão:** Alterar apenas o **CSS** para limitar a largura da linha, ajustar o `line-height`, trocar a fonte e melhorar o contraste. Deixe o texto prazeroso de ler.

---

## 🚀 Atividade 3: WCAG Avançado (Portal Acadêmico)
**Arquivo:** `9-Desafio-WCAG-Avancado.html`

**O Desafio:** Este é um portal completo com múltiplos erros de acessibilidade que afetam diferentes tipos de deficiência.
1. **Imagens:** Como um deficiente visual saberia o que está na foto da notícia?
2. **Links Ambíguos:** Encontre o link "Clique aqui". Se o usuário listar apenas os links da página, ele saberá para onde esse link leva?
3. **Estados de Interface:** O botão "[+] Dúvidas frequentes" é um `div`. Como um leitor de tela avisa ao usuário que aquele conteúdo expandiu?
4. **Uso de Cor:** Identifique onde a cor é usada como única forma de passar uma instrução obrigatória. Como um daltônico veria isso?

**Sua missão:** Refatorar o portal aplicando:
- Tags semânticas (`<main>`, `<nav>`, `<article>`, `<h1>`).
- Atributos ARIA (`aria-label`, `aria-expanded`, `aria-required`).
- Textos alternativos descritivos e links contextuais.

---

### 🔍 Ferramentas Recomendadas
*   **Extensão WAVE:** Para auditoria visual instantânea.
*   **Chrome DevTools (Lighthouse):** Aba "Acessibilidade".
*   **NVDA ou VoiceOver:** Para testar como o sistema "soa".
