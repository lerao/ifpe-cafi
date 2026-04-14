#Alternativa de resposta 1
nota = int(input("Digite uma nota entre 0 e 10: "))

while nota < 0 or nota > 10:
    print("Valor inválido!")
    nota = int(input("Digite novamente: "))

print("Nota válida:", nota)

#Alternativa de resposta 2
while True:
    nota = int(input("Digite uma nota entre 0 e 10: "))
    if 0 <= nota <= 10:
        print("Nota válida:", nota)
        break
    else:
        print("Valor inválido! Tente novamente.")
