def finalizarCompra(CARRINHO:list) -> None:
    total = 0
    for p in CARRINHO:
        subtotal = p[1]*p[2]
        total = total + subtotal
        print(f'{p[0]} - R$ {p[1]} - Qtd: {p[2]} = R$ {subtotal}')
    
    forma = str(input("Informe a forma de pagamento: "))
    endereco = str(input("Informe o endereço de entrega: "))

    print(f'''
            {'*'*30}
            Finalização
            {'*'*30} 

            Endereço: {endereco}
            Forma de Pagamento: {forma}
            ======
            Total R$ {total}

            ''')

def menuPrincipal() -> None:
    print('''
        Escolha uma opção:
        1 - Lista de produtos
        2 - Carrinho de compras
        3 - Pagamento e Finalização
        4 - Sair do sistema
        ''')
    
def sair() -> None:
    print('Encerrado! Até logo!')

def listarProdutos(PRODUTOS: list) -> None:
    cont = 0
    for produto in PRODUTOS:
        cont += 1
        print(f'{cont}: {produto[0]} - R$ {produto[1]}')

def adicionarCarrinho(CARRINHO:list, PRODUTOS:list) -> None:
    print("Qual produto deseja adicionar ao carrinho? ")
    escolhido = int(input())
    qtd = int(input("Quantos deseja? "))
    produtoEscolhido = PRODUTOS[escolhido-1]
    produtoEscolhido.append(qtd)
    CARRINHO.append(produtoEscolhido)