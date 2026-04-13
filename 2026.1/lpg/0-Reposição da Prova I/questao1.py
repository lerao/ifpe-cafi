#Faça um programa que receba 3 números, calcule a média e informe se o aluno está aprovado ou não. Para ser aprovado o aluno precisa ter a média igual ou superior a 7.

# Recebe os números do usuário
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

# Calcula a média
media = (nota1 + nota2 + nota3) / 3

# Verifica se o aluno está aprovado ou não
if media >= 7:
    print("Aluno aprovado! Média:", media)
else:
    print("Aluno reprovado! Média:", media)
