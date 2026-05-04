#Funções/Métodos
def qtdVogais(texto) -> int:
    vogais = 0
    for letra in texto.lower():
        if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
                vogais = vogais + 1
    return vogais
