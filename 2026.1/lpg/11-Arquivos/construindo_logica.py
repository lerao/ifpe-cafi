#Lógica de String para Lista
produtos_str = "Farinha,Açúcar,Café"
lista = produtos_str.split(",")
print(lista)

#Lógica de Lista para String
produtos = ['Feijão','Arroz','Macarrão']
#Feijão,Arroz,Macarrão
string = ""
for produto in produtos:
    if string != "":
        string = string + "," + produto
    else:
        string = produto
print(string)


