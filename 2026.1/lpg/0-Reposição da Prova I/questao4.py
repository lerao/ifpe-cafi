#Crie um programa que receba a distância que será percorrida e o consumo do carro.
#Por fim, informe quanto será gasto de gasolina para realizar ida e volta nessa
#viagem considerando o preço da gasolina de R$ 6,60

# Recebe a distância e o consumo do carro do usuário
distancia = float(input("Digite a distância a ser percorrida (em km): "))
consumo = float(input("Digite o consumo do carro (em km/l): "))

# Define o preço da gasolina
preco_gasolina = 6.60

# Calcula a quantidade de gasolina necessária para a viagem de ida e volta
quantidade_gasolina = (distancia * 2) / consumo

# Calcula o custo total da gasolina
custo_total = quantidade_gasolina * preco_gasolina

# Exibe o resultado
print(f"O custo total da gasolina para a viagem de ida e volta é: R$ {custo_total:.2f}")
