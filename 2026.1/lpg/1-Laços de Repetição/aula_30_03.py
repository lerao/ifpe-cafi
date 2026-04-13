"""
30/03/2026 
- Resolução das questões da prova de recuperação;
- Introdução às estruturas de repetição: while e for;


Estruturas de Repetição:
-while
-for

while (condicao):
  condicao_true

- break: para imediatamente a execução do meu laço de repetição

- For
for (para)
range(start, stop, step)
      -> (0, 5, 1) -> 0, 1, 2, 3, 4
      -> (2, 11, 2) -> 2, 4, 6, 8, 10

#SINTAXE BASE DO FOR
for variavel in range(start, stop, step):
   print(variavel)
"""
# Exemplo do while para solicitar uma letra indefinidade
# até que o usuário informe a letra S ou s para encerrar o programa
while True:
    letra = input("Informe uma letra: ")
    if letra == 'S' or letra == 's':
        print("Até logo")
        break

# Exemplo do for para imprimir os números de 1 a 10
for par in range(2, 11, 2):
    print(par)

#Exemplo do range para calcular a soma dos números pares de 1 a 1000
soma = 0
for elemento in range(2, 1001, 2):
    soma = soma + elemento
print(soma)

#É possível iterar sobre uma string
for letra in "Afogados":
    print(letra)

#Erro pois 10 não é um objeto iterável
for n in 10:
    print(n)