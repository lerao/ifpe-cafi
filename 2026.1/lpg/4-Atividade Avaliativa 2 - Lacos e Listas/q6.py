#Não precisa colocar a lista novamente na prova'
processos = [
    ["0001111-22.2023.8.26.0100", "Ana Costa", 50000],
    ["0002222-33.2022.8.19.0001", "Bruno Lima", 30000],
    ["0003333-44.2023.8.13.0005", "Ana Costa", 75000]
]

#Somar o valor total dos processos
total = 0
for processo_individual in processos:
    total = total = processo_individual[2]

print("Valor total das causas:", total)