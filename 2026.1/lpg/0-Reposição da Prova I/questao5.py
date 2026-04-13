#Faça um programa de uma calculadora básica, onde deve solicitar um número,
#posteriormente solicitar uma operação (1 = soma, 2 = subtração, 3 = multiplicação, 4
#= produto), em seguida solicitar outro número e mostrar o resultado.

# Recebe o primeiro número do usuário
num1 = float(input("Digite o primeiro número: "))

# Solicita a operação desejada
print("Escolha a operação:")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")
operacao = int(input("Digite o número da operação: "))
# Recebe o segundo número do usuário
num2 = float(input("Digite o segundo número: "))
# Realiza a operação escolhida e exibe o resultado
if operacao == 1:
    resultado = num1 + num2
    print(f"Resultado da soma: {resultado}")
elif operacao == 2:
    resultado = num1 - num2
    print(f"Resultado da subtração: {resultado}")
elif operacao == 3:
    resultado = num1 * num2
    print(f"Resultado da multiplicação: {resultado}")
elif operacao == 4:
    if num2 != 0:
        resultado = num1 / num2
        print(f"Resultado da divisão: {resultado}")
    else:
        print("Erro: Divisão por zero não é permitida.")
else:
    print("Operação inválida. Por favor, escolha uma operação entre 1 e 4.")
