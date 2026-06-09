# Guia de Aula: Conectando PHP ao Banco de Dados com PDO
---

## 1. O que é o Banco de Dados?
Imagine o banco de dados como uma planilha de Excel gigante e organizada, onde o PHP pode ler e escrever informações. Usamos a linguagem **SQL** para conversar com ele.

### O Arquivo `banco.sql`
Neste arquivo, definimos a estrutura:
- **Tabela `usuarios`**: Guarda quem pode entrar no sistema.
- **Tabela `transacoes`**: Guarda cada depósito ou saque feito.

---

## 2. A Ponte: `conexao.php`
Para o PHP "falar" com o MySQL, usamos o **PDO (PHP Data Objects)**. Ele é como um tradutor universal. No arquivo `conexao.php`, configuramos o endereço do banco (`localhost`), o nome (`sistema_bancario`), o usuário (`root`) e a senha.

---

## 3. O Login Dinâmico (`validalogin.php`)
Antes, tínhamos um `if` fixo: `if ($usuario == 'admin')`. Isso é ruim porque só existia um usuário.
Agora fazemos uma **Consulta (SELECT)**:
1. "Ei Banco, me dá os dados do usuário que tem o login que a pessoa digitou?"
2. Se o banco encontrar, conferimos a senha.
3. Se estiver tudo certo, guardamos o `ID` e o `Nome` da pessoa na **Sessão** para saber quem ela é nas outras páginas.

> **Dica de Segurança:** Usamos `?` na consulta (Prepared Statements) para evitar que hackers tentem "quebrar" nosso comando SQL.

---

## 4. Salvando Informações (`processa_transacao.php`)
Quando você preenche o formulário na página principal, o PHP executa um comando **INSERT**:
```sql
INSERT INTO transacoes (usuario_id, tipo, valor) VALUES (?, ?, ?)
```
Isso "carimba" no banco de dados que aquele usuário específico fez um depósito de X reais.

---

## 5. Mostrando o Histórico (`historico.php`)
Para mostrar os dados, usamos outro **SELECT**, mas agora pegamos todos os registros da tabela de transações que pertencem ao usuário logado. Usamos um `foreach` (um laço de repetição) para criar as linhas da tabela HTML automaticamente.

---

## 🚀 Desafio Final: Seu Projeto!
Agora que você viu como funciona um sistema bancário, que tal criar o seu próprio sistema. Exemplo: **Sistema de Biblioteca**

**O que o sistema deve fazer (atrelado ao seu contexto de trabalho):**
1. **Login**: Alunos ou bibliotecários entram com usuário e senha.
2. **Lista de Livros**: Uma página que mostra os livros cadastrados no banco de dados.
3. **Empréstimo**: Um formulário onde o aluno escolhe um livro e clica em "Pegar Emprestado".
4. **Meu Histórico**: Uma página que mostra quais livros aquele aluno já pegou.

**Dica de Tabelas:**
- `usuarios` (id, nome, login, senha)
- `livros` (id, titulo, autor, disponivel)
- `emprestimos` (id, usuario_id, livro_id, data_emprestimo)

Entrega via classroom!