# Faça um programa que receba um número e diga se ele é múltiplo de 2,3,5 ou 7 informe se ele é par ou ímpar. Exemplo: caso informe o número 15. irá imprimir :
#Múltiplo de 3.
#Múltiplo de 5.

# Recebe o número do usuário
numero = int(input("Digite um número: "))

# Verifica se o número é múltiplo de 2, 3, 5 ou 7
if numero % 2 == 0:
    print("Múltiplo de 2.")
if numero % 3 == 0:
    print("Múltiplo de 3.")
if numero % 5 == 0:
    print("Múltiplo de 5.")
if numero % 7 == 0:
    print("Múltiplo de 7.")