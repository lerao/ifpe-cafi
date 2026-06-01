with open("bd.txt","r",
          encoding="utf-8") as arquivo:
    for linha in arquivo:
        lista = linha.split(",")
    print(lista)

#lista = ['Farinha','Açúcar','Café']
prod = input("Informe um produto: ")

#lista = ['Farinha','Açúcar','Café', 'Feijão']
lista.append(prod)

string = ""
for elemento in lista:
    if string == "":
        string = elemento
    else:
        string += "," + elemento

with open("bd.txt", "w",
          encoding="utf-8") as arquivo:
    arquivo.write(string)
