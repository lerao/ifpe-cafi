#Passos: 
# 0 - Entender a estrutura de listas dentro de listas [[],[]]
# 1 - Criar os for's para representar as posições Linhas e Colunas: 0,0 0,1 1,0 1,1 ...
# 2 - Receber os valores individuais do usuário para cada posição
# 3 - Criar as linhas e ir 'povoando' guardando os valores
# 4 - Criar uma função genérica para gerar qualquer matriz
# 5 - Receber os dados do usuário e gerar as matrizes

#Para pensar: como fazer o mesmo usando While ?????

def criarMatriz(linhas, colunas):
    matriz = []
    for linha in range(0, linhas, 1):
        lista = []
        for coluna in range(0, colunas, 1):
            print(f"[{linha}][{coluna}]")
            valor = int(input("Informe um valor: "))
            lista.append(valor)
        matriz.append(lista)
    return matriz
qtdLinhas = int(input("Informe a qtd de linhas: "))
qtdColunas = int(input("Informe a qtd de colunas: "))
print(criarMatriz(qtdLinhas, qtdColunas))