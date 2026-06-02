#Lógica por trás do sum() lista
lista = [10,20,30,40,50]
soma = 0
for x in lista:
    soma = soma + x
print(soma)


#Decimal para binário
c=int(input("Digite um numero: "))
lista=[]
while c>0:
    divisao=c%2
    lista.append(divisao)
    c=c//2
binario = ""
for i in range(len(lista)-1,-1,-1):
    binario += str(lista[i])
print(f"o numero em binário é {binario}")


#Número binário para decimal
c = 0
soma = 0
binario = str(input("digite o numero binario: "))
for x in range(len(binario)-1,-1,-1):
    mult = int(binario[x]) * 2**c
    c += 1
    soma += mult  
print(soma)