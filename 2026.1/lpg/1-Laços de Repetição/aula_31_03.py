"""
31/03/2026
Revisão e resolução de questões;
"""

#1
for n in range(1,11,1):
    print(n)

#2 e 3
senha="senha"
qtd_erros = 0
while True:
    senha_usuario = input("Informe uma senha")
    if senha_usuario == senha:
        print("Login efetuado!")
        print("Total de erros = ", qtd_erros)
        break
    else:
        print("Senha incorreta")
        qtd_erros = qtd_erros + 1