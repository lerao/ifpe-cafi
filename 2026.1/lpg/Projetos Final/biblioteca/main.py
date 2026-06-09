from gerenciador_arquivos import GerenciadorArquivo

def menu():
    print("\n" + "="*30)
    print("     SISTEMA DE BIBLIOTECA")
    print("="*30)
    print("1. Cadastrar Livro")
    print("2. Listar Todos os Livros")
    print("3. Registrar Empréstimo")
    print("4. Registrar Devolução")
    print("0. Sair")
    print("="*30)

def cadastrar_livro(db):
    print("\n--- Cadastro de Livro ---")
    titulo = input("Título: ")
    autor = input("Autor: ")
    ano = int(input("Ano de Publicação: "))
    
    livros = db.recuperaDados()
    # Estrutura: [ID, Título, Autor, Ano, Status]
    proximo_id = len(livros) + 1
    status = "Disponível"
    
    livros.append([proximo_id, titulo, autor, ano, status])
    db.salvarDados(livros)
    print(f"Livro '{titulo}' cadastrado com ID {proximo_id}!")

def listar_livros(db):
    print("\n--- Acervo da Biblioteca ---")
    livros = db.recuperaDados()
    if not livros:
        print("A biblioteca está vazia.")
        return
    
    for l in livros:
        print(f"ID: {l[0]} | {l[1]} ({l[3]}) - {l[2]} | Status: {l[4]}")

def alterar_status(db, status_novo):
    listar_livros(db)
    livros = db.recuperaDados()
    if not livros: return
    
    try:
        id_livro = int(input(f"\nDigite o ID do livro para {status_novo.lower()}: "))
        encontrado = False
        for l in livros:
            if l[0] == id_livro:
                l[4] = status_novo
                encontrado = True
                break
        
        if encontrado:
            db.salvarDados(livros)
            print(f"Status atualizado para: {status_novo}")
        else:
            print("Livro não encontrado.")
    except ValueError:
        print("Erro: Digite um número válido para o ID.")

def principal():
    db_livros = GerenciadorArquivo("livros.csv")
    
    while True:
        menu()
        opcao = input("Opção: ")
        
        if opcao == "1":
            cadastrar_livro(db_livros)
        elif opcao == "2":
            listar_livros(db_livros)
        elif opcao == "3":
            alterar_status(db_livros, "Emprestado")
        elif opcao == "4":
            alterar_status(db_livros, "Disponível")
        elif opcao == "0":
            print("Encerrando sistema... Até mais!")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    principal()
