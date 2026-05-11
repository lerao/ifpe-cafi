****** Revisão Geral ******
1. Peça ao usuário para digitar o nome e exiba ele invertido. (strings/listas + input + print)
nome = input("Digite um nome: ")
tamanho = len(nome)
nome_i = ""
for pos in range(tamanho-1, -1, -1):
    nome_i = nome_i + nome[pos]

print(nome_invertido)



2. Peça ao usuário para digitar 3 itens de uma lista de compras e depois mostre:
Todos os itens
Quantos itens foram digitados
(listas + loop)

compras = []
for i in range(0,3,1):
    produto = input("Informe o produto: ")
    compras.append(produto)

for produto in compras:
    print(f"Produto: {produto}")

print(f"Tamanho da lista: {len(compras)}")




3. Crie uma função que receba uma palavra ou frase e retorne quantas vogais existem nela. Depois, peça ao usuário uma entrada e use a função para mostrar o resultado.
(funções + strings + lógica)