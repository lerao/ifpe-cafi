#1.	Crie uma função que transforma todos os caracteres de uma string em maiúsculos
def tudoMaiusc(str):
    return str.upper()

print(tudoMaiusc("teste"))

#2.	Crie uma função que transforma todos os caracteres de uma string em maiúsculos
def tudoMinusc(str):
    return str.lower()
print(tudoMinusc("TESTE"))

#3.	Crie uma função que remova as vogais de uma string
def removerVogais(str):
    str = str.replace("a", "")#cabelo->cbelo
    str = str.replace("e", "")#cbelo->cblo
    str = str.replace("i", "")#cblo
    str = str.replace("o", "")#cbl
    str = str.replace("u", "")#cbl
    return str  
print(removerVogais("cabelo"))

#4.	Crie uma função que informe o tamanho de uma string (não utilize a função len)
def informarTamanho(str):
    contador = 0
    for c in str:
        contador += 1
    return contador

print(informarTamanho("cabelo"))

#5.	Crie uma função que recebe uma string e um caractere, e retorne o número de vezes que esse caractere aparece na string.
#sem usar o count
def contarCaractere(str, c):
    contador = 0
    for caractere in str:
        if caractere == c:
            contador += 1
    return contador
print(contarCaractere("cabelo", "a"))
#usando o count
def contarCaractere2(str, c):
    return str.count(c)
print(contarCaractere2("cabelo", "a"))

#6.	Crie uma função que recebe uma string e um caractere, e apague todas as ocorrências desses caractere na string.
def apagarCaractere(str, c):
    return str.replace(c, "")
print(apagarCaractere("banana", "a"))

#7.	Faça uma função que retorne uma lista com as letras que se repetiram e quantas vezes repetiram
def letrasRepetidas(str):
   letrasRepetidas = []
   for letra in str:
       if str.count(letra) > 1:
        letraQtd = [letra, str.count(letra)]
        if letraQtd not in letrasRepetidas:
            letrasRepetidas.append(letraQtd)
   return letrasRepetidas
print(letrasRepetidas("banana"))

#8.	Faça uma função que receba uma string, um índice e outra string, a função irá sobrescrever a velha string (1º parâmetro) com a nova string (3º parâmetro) a partir do índice informado (2º parâmetro).
def sobrescreverString(string_velha, indice, string_nova):
    resultado = string_velha[:indice] + string_nova
    fim_da_substituicao = indice + len(string_nova)
    resultado += string_velha[fim_da_substituicao:]
    return resultado

print(sobrescreverString("PythoN te gosto!", 10, "adoro"))

#9.	Faça um programa em que troque todas as ocorrencias de uma letra L1 pela letra L2 em uma string. A string e as letras L1 e L2 devem ser fornecidas pelo usuario. ( não utilize a função replace)
def trocarLetras(str, l1, l2):
    resultado = ""
    for c in str:
        if c == l1:
            resultado = resultado + l2
        else:
            resultado = resultado + c
    return resultado

#10.	Crie uma função que duplique cada caractere da string
def duplicarCaracteres(str):
    resultado = ""
    for c in str:
        resultado += c * 2
    return resultado
print(duplicarCaracteres("cabelo"))