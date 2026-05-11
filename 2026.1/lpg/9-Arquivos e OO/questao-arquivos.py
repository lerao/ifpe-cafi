def cadastrar_produto():
    
    """Solicita dados do usuário e salva no arquivo produtos.txt"""

    print("\n--- Cadastro de Novo Produto ---")
    codigo = input("Digite o código do produto: ")
    descricao = input("Digite a descrição: ")
    preco = input("Digite o preço (ex: 50.00): ")

    # Abrindo no modo 'a' (append) para não sobrescrever dados anteriores
    with open("produtos.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"{codigo};{descricao};{preco}\n")
    print("Produto cadastrado com sucesso!")


def calcular_soma_precos():
    """Lê o arquivo e calcula a soma total de todos os produtos"""
    soma_total = 0.0
    print("\n--- Relatório de Preços ---")
    
    with open("produtos.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            # Remove espaços/quebras e divide pelo delimitador ';'
            dados = linha.strip().split(";")
            
            # Verifica se a linha possui os 3 campos (evita erros em linhas vazias)
            if len(dados) == 3:
                preco = float(dados[2])
                soma_total += preco
    
    print(f"Soma total dos produtos em estoque: R$ {soma_total:.2f}")
   

# Menu simples para execução
#A instrução if __name__ == "__main__": em Python serve para garantir que um bloco de código seja 
# executado apenas quando o arquivo for rodado diretamente, e não quando 
# for importado como um módulo em outro script
if __name__ == "__main__":
    while True:
        print("\n1. Cadastrar Produto")
        print("2. Calcular Soma Total")
        print("3. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_produto()
        elif opcao == "2":
            calcular_soma_precos()
        elif opcao == "3":
            break
        else:
            print("Opção inválida.")