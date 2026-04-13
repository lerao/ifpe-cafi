senhas = [
    ['Lairson', '123'],
    ['Maria', 'senha'],
    ['Sicrano', 'abc']
]
print("*** Bem vindo(a)")
cont = 0
while cont == 0:
    print("Informe uma senha para entrar")
    senha_digitada = input("")
    for usuario in senhas:
        if (usuario[1] == senha_digitada):
            print("Bem vindo(a)", usuario[0])
            cont = cont + 1
            break
    if cont == 0:
        print("Senha incorreta!")