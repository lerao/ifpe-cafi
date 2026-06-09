from gerenciador_arquivos import GerenciadorArquivo

def menu():
    print("\n" + "="*30)
    print("      CONTROLE DE ESTOQUE")
    print("="*30)
    print("1. Cadastrar Produto")
    print("2. Listar Estoque")
    print("3. Atualizar Quantidade")
    print("4. Registrar Venda")
    print("0. Sair")
    print("="*30)

def cadastrar_produto(db):
    print("\n--- Novo Produto ---")
    nome = input("Nome do Produto: ")
    preco = float(input("Preço Unitário: "))
    qtd = int(input("Quantidade Inicial: "))
    
    produtos = db.recuperaDados()
    # [Nome, Preço, Quantidade]
    produtos.append([nome, preco, qtd])
    db.salvarDados(produtos)
    print("Produto cadastrado!")

def listar_estoque(db):
    print("\n--- Relatório de Estoque ---")
    produtos = db.recuperaDados()
    if not produtos:
        print("Estoque vazio.")
        return
    
    for p in produtos:
        print(f"Produto: {p[0]:15} | Preço: R$ {p[1]:7.2f} | Qtd: {p[2]}")

def atualizar_quantidade(db):
    listar_estoque(db)
    produtos = db.recuperaDados()
    if not produtos: return
    
    nome_busca = input("\nNome do produto para atualizar: ")
    encontrado = False
    for p in produtos:
        if p[0].lower() == nome_busca.lower():
            nova_qtd = int(input(f"Nova quantidade para {p[0]}: "))
            p[2] = nova_qtd
            encontrado = True
            break
            
    if encontrado:
        db.salvarDados(produtos)
        print("Quantidade atualizada!")
    else:
        print("Produto não encontrado.")

def registrar_venda(db):
    listar_estoque(db)
    produtos = db.recuperaDados()
    if not produtos: return
    
    nome_busca = input("\nNome do produto vendido: ")
    encontrado = False
    for p in produtos:
        if p[0].lower() == nome_busca.lower():
            qtd_venda = int(input(f"Quantidade vendida: "))
            if p[2] >= qtd_venda:
                p[2] -= qtd_venda
                total = qtd_venda * p[1]
                print(f"Venda realizada! Total: R$ {total:.2f}")
                encontrado = True
            else:
                print("Estoque insuficiente!")
                return
            break
            
    if encontrado:
        db.salvarDados(produtos)
    else:
        print("Produto não encontrado.")

def principal():
    db_estoque = GerenciadorArquivo("estoque.csv")
    
    while True:
        menu()
        opcao = input("Opção: ")
        
        if opcao == "1":
            cadastrar_produto(db_estoque)
        elif opcao == "2":
            listar_estoque(db_estoque)
        elif opcao == "3":
            atualizar_quantidade(db_estoque)
        elif opcao == "4":
            registrar_venda(db_estoque)
        elif opcao == "0":
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    principal()
