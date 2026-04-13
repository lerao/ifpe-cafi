#listas
#lista_vazia = []
#lista = [1, 2, 3]
#lista_nao_vazia = ["A", 2, 3.4, True, []]

#sum(lista)
#soma os valores da lista - qdo númericas

#max(lista)
#maior elemento da lista

#min(lista)
#menor elemento da lista

#lista.count(elemento)
#conta quantos ocorrências do elemento existe na lista

#len(lista)
#tamanho da lista

#lista.append(elemento)
#insere o elemento na última posição da lista (no final)

#elemento in lista
#verifica se o elemento existe na lista

#for elemento in lista
#percorrer os elementos da minha lista

#listas com mais de uma dimensão
#[[],[],[]]

#python cria indices automaticamente
#acessar uma posição -> index out of range

#insert(posicao, elemento) 
#insere o elemento de forma segura na posição especificada
# qdo a posição não existe, ele insere na última posição

#lista = [10,20]
#lista2 = lista
#lista2.append(5)
#lista e lista2 vão ter o mesmo valor
#devido a questões de não ser imutável

#lista.extend(lista2)
#insere os elementos de lista2 em lista

#lista4 = lista.copy()
#faz uma cópia completa do objeto/valores
#não faz a cópia da referência da memória

#lista.pop()
#remove o último elemento da lista
#retorna o valor do elemento removido
#lista.pop(posicao)
#remove o elemento na posicao especificada
#a remoção só remove o primeiro elemento encontrado

#lista.remove(valor) 
#remove o valor do elemento se ele existir na lista

#clear() 
#remove todos os elementos da lista

#index() 
#retorna a posição do primeiro elemento encontrado na lista

#reverse() 
#obtém uma lista com posições reversas

#sort()
#ordena a lista de forma ascedente

#sort(reverse=True)
#ordena a lista de forma descendente

#Exercícios

#Crie um menu com as seguintes opções:
#1) Cadastrar
#2) Buscar
#3) Deletar
#4) Listar
#0) Sair

''' 
LISTA_TELEFONICA = []
while True:
    print('' '
    Escolha uma opção:
        1) Cadastrar
        2) Buscar
        3) Deletar
        4) Listar
        0) Sair'' ')
    opcao = int(input("Informe a opção: "))
    if opcao == 0:
        print("Até logo!")
        break
    elif opcao == 1:
        tel = str(input("Informe o telefone: "))
        LISTA_TELEFONICA.append(tel)
    elif opcao == 2:
        tel_buscando = str(input("Informe o telefone: "))
        if tel_buscando in LISTA_TELEFONICA:
            print("Telefone encontrado.")
        else:
            print("Telefone NÃO encontrado")
    elif opcao == 3:
        tel_buscando = str(input("Informe o telefone: "))
        if tel_buscando in LISTA_TELEFONICA:
            LISTA_TELEFONICA.remove(tel_buscando)
            print(tel_buscando, " foi deletado com sucesso.")
        else:
            print("Telefone NÃO encontrado")
    elif opcao == 4:
        LISTA_TELEFONICA.sort()
        for tel in LISTA_TELEFONICA:
            print("Telefone: ", tel)

'''

LISTA_TELEFONICA = []
while True:
    print('''
    Escolha uma opção:
        1) Cadastrar
        2) Buscar
        3) Deletar
        4) Listar
        5) Alterar um telefone ou nome
        0) Sair
          ''')
    opcao = int(input("Informe a opção: "))
    if opcao == 0:
        print("Até logo!")
        break
    elif opcao == 1:
        #['81', '811']
        #[ ['81','Nome'],  ['811', 'Outro'] ]
        tel = str(input("Informe o telefone: "))
        nome = str(input("Informe o nome: "))
        pessoa = [tel, nome]
        LISTA_TELEFONICA.append(pessoa)
    elif opcao == 2:
        tel_buscando = str(input("Informe o telefone: "))
        encontrou = False
        for pessoa in LISTA_TELEFONICA:
            if tel_buscando == pessoa[0]:
                print("Contato encontrado: ", pessoa[1])
                encontrou = True
                break
        if encontrou == False:
            print("Telefone NÃO encontrado")
    elif opcao == 3:
        tel_buscando = str(input("Informe o telefone: "))
        for pessoa in LISTA_TELEFONICA:
            if tel_buscando == pessoa[0]:
                LISTA_TELEFONICA.remove(pessoa)
                print('Pessoa removida: ', pessoa[1])
                break
            else:
                print("Telefone NÃO encontrado")
    elif opcao == 4:
        #LISTA_TELEFONICA.sort()
        for pessoa in LISTA_TELEFONICA:
            print("Nome: ", pessoa[1], " | Telefone: ", pessoa[0])
