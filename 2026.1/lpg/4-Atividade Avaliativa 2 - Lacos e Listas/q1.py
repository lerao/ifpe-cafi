c1 = 0
c2 = 0 
c3 = 0
c4 = 0

#Devido a imutabilidade das variáveis inteiras
#poderíamos criar as variáveis assim:
#c1 = c2 = c3 = c4 = 0

num = int(input("Digite um número: "))

while num >= 0:
    #uma outra forma de escrever os ifs seria:
    # if 0 <= num <= 25:
    # elif 26 <= num <= 50:
    # elif 51 <= num <= 75:
    # elif 76 <= num <= 100:
    # ou seja, usando o operador de comparação encadeada, que é mais legível e fácil de entender.
    # semelhante a uma expressão matemática/intervalo, onde o número deve estar entre os limites definidos.
    if 0 <= num and num <= 25:
        c1 += 1
    elif 26 <= num and num <= 50:
        c2 += 1
    elif 51 <= num and num <= 75:
        c3 += 1
    elif 76 <= num and num <= 100:
        c4 += 1

    num = int(input("Digite um número: "))

print("[0-25]:", c1)
print("[26-50]:", c2)
print("[51-75]:", c3)
print("[76-100]:", c4)