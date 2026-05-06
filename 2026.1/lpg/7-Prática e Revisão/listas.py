
def adicionar_elemento(lista: list, elemento: str) -> bool:
    '''
    Verifica se o elemento começa com letra maiúscula
    Se ele passar na verificação, inserir na lista e retornar
    verdadeiro, caso contrário, retorne falso
    '''
    letra1 = elemento[0]
    if (letra1 == letra1.upper()):
        lista.append(elemento)
        return True
    else:
        return False
    
def buscar_elemento(lista: list, elemento: str) -> bool:
    '''
    Verifica se um elemento está contido na lista.
    Se estiver, retorne verdadeiro, caso contrário, retorne falso.
    '''
    return elemento in lista

def remover_elemento(lista: list, elemento: str) -> bool:
    '''
    Verifica se a lista contém um elemento específico.
    Se ele estiver contido na lista, remover o elemento e
    retornar verdadeiro, caso contrário, retornar falso.
    '''
    if elemento in lista:
        lista.remove(elemento)
        return True 
    else:
        return False

def limpar_lista(lista: list) -> None:
    '''
    Remove todos os elementos da lista.
    Função sem retorno.
    '''
    lista.clear()

def ordenar_lista(lista: list) -> None:
    '''
    Ordena todos os elementos da lista por ordem
    alfabética. A função não possui retorno
    '''
    lista.sort()

def pegar_quantidade(lista: list) -> int:
    '''
    Retorna a quantidade de elementos dentro
    da lista
    '''
    return len(lista)

def converter_maiusculo(lista: list) -> list:
    '''
    Converte todos os elementos da lista para letra
    maiúscula e os retorna em uma nova lista
    '''
    listaFinal = []
    for el in lista:
        listaFinal.append(el.upper())
    return listaFinal

def eliminar_repetidos(lista: list) -> list:
    '''
    DESAFIO: 0.5 extra
    Remove todos os elementos repetidos na lista
    e retorna uma lista nova (não vale utilizar o set)
    '''
    lista_nova = []
    for el in lista:
        if el not in lista_nova:
            lista_nova.append(el)
    return lista_nova