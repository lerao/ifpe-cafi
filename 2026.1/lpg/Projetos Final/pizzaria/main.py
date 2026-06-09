from gerenciador_arquivos import GerenciadorArquivo

def menu():
    print("\n" + "="*30)
    print("      PIZZARIA PYTHON")
    print("="*30)
    print("1. Cadastrar Pizza")
    print("2. Listar Cardápio")
    print("3. Realizar Pedido")
    print("4. Relatório de Vendas")
    print("0. Sair")
    print("="*30)

def cadastrar_pizza(gerenciador):
    print("\n--- Cadastro de Nova Pizza ---")
    nome = input("Nome da Pizza: ")
    preco = float(input("Preço: "))
    
    # Recupera o cardápio atual
    cardapio = gerenciador.recuperaDados()
    
    # Gera um ID simples
    proximo_id = len(cardapio) + 1
    
    # Adiciona a nova pizza
    cardapio.append([proximo_id, nome, preco])
    
    # Salva de volta
    gerenciador.salvarDados(cardapio)
    print("Pizza cadastrada com sucesso!")

def listar_cardapio(gerenciador):
    print("\n--- Cardápio Atual ---")
    cardapio = gerenciador.recuperaDados()
    
    if not cardapio:
        print("Cardápio vazio.")
        return
        
    for pizza in cardapio:
        print(f"ID: {pizza[0]} | Nome: {pizza[1]} | Preço: R$ {pizza[2]:.2f}")

def realizar_pedido(gerenciador_cardapio, gerenciador_vendas):
    print("\n--- Novo Pedido ---")
    listar_cardapio(gerenciador_cardapio)
    
    cardapio = gerenciador_cardapio.recuperaDados()
    if not cardapio:
        return

    try:
        id_escolhido = int(input("\nDigite o ID da pizza que deseja: "))
        
        pizza_encontrada = None
        for pizza in cardapio:
            if pizza[0] == id_escolhido:
                pizza_encontrada = pizza
                break
        
        if pizza_encontrada:
            quantidade = int(input(f"Quantas unidades de '{pizza_encontrada[1]}'? "))
            total = pizza_encontrada[2] * quantidade
            print(f"Total do pedido: R$ {total:.2f}")
            
            # Salvar a venda: [Nome, Quantidade, Valor Total]
            vendas = gerenciador_vendas.recuperaDados()
            vendas.append([pizza_encontrada[1], quantidade, total])
            gerenciador_vendas.salvarDados(vendas)
            print("Pedido registrado!")
        else:
            print("ID de pizza não encontrado.")
    except ValueError:
        print("Entrada inválida. Digite números.")

def relatorio_vendas(gerenciador_vendas):
    print("\n--- Relatório de Vendas ---")
    vendas = gerenciador_vendas.recuperaDados()
    
    if not vendas:
        print("Nenhuma venda realizada ainda.")
        return
    
    total_geral = 0
    for v in vendas:
        print(f"Pizza: {v[0]} | Qtd: {v[1]} | Subtotal: R$ {v[2]:.2f}")
        total_geral += v[2]
    
    print("-" * 20)
    print(f"FATURAMENTO TOTAL: R$ {total_geral:.2f}")

def principal():
    # Inicializa os gerenciadores de arquivos
    # Um para o cardápio e outro para as vendas (histórico)
    db_cardapio = GerenciadorArquivo("cardapio.csv")
    db_vendas = GerenciadorArquivo("vendas.csv")
    
    while True:
        menu()
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            cadastrar_pizza(db_cardapio)
        elif opcao == "2":
            listar_cardapio(db_cardapio)
        elif opcao == "3":
            realizar_pedido(db_cardapio, db_vendas)
        elif opcao == "4":
            relatorio_vendas(db_vendas)
        elif opcao == "0":
            print("Saindo do sistema da Pizzaria. Até logo!")
            break
        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    principal()
