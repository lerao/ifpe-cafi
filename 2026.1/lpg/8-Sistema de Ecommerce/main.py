import funcoes 

PRODUTOS = [
    ['PIZZA', 50],
    ['TRELOSO', 2],
    ['FANDAGOS', 3.5],
    ['SUSHI', 5],
    ['ESPETINHO', 6]
]

CARRINHO = []

while True:
    funcoes.menuPrincipal()
    opcao = int(input("Opção = "))
    if opcao == 4:
        funcoes.sair()
        break
    elif opcao == 1:
        funcoes.listarProdutos(PRODUTOS)
    elif opcao == 2:
        funcoes.listarProdutos(PRODUTOS)
        while True:
            funcoes.adicionarCarrinho(CARRINHO, PRODUTOS)
            print("O que deseja fazer?")
            print("1: Finalizar compra")
            print("2: Continuar comprando")
            print("3: Voltar ao menu principal")
            opcaoCarrinho = int(input())
            if opcaoCarrinho == 1:
                funcoes.finalizarCompra(CARRINHO)
                break
            elif opcaoCarrinho == 3: 
                break
    elif opcao == 3:
        funcoes.finalizarCompra(CARRINHO)
        break
