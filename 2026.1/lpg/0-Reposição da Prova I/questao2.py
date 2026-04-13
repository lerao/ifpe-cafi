# Faça um algoritmo que receba o salário de uma pessoa e informe o equivalente emsalários mínimos. Caso o número de salários mínimos não seja exato informe o texto “um pouco mais de X salários mínimos” (Salário mínimo é de R$1621,00). Exemplo: informar 3500.00
#um pouco mais de 2 salários mínimos

# Define o salário mínimo
salario_minimo = 1621.00

# Recebe o salário do usuário
salario = float(input("Digite o salário: "))

# Calcula o número de salários mínimos
num_salarios_minimos = salario // salario_minimo

# Verifica se o número de salários mínimos é exato ou não
#if num_salarios_minimos.is_integer():
if salario % salario_minimo == 0:
    print(f"equivalente a {int(num_salarios_minimos)} salários mínimos.")
else:
    print(f"um pouco mais de {int(num_salarios_minimos)} salários mínimos.")  
