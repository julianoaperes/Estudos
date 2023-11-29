# Criação das listas vazias
carros = []
consumo_gasolina = []

# Dados para cálculo do consumo 
distancia = 500
custo_gasolina = 4.90

while True:
    carro = input("Digite o nome do carro ou digite 'sair' para encerrar: ")
    
    if carro.lower() == 'sair':
        print("Obrigado por sua participação!")
        break    
    
    consumo = float(input(f"Digite o consumo de gasolina por litro para o {carro} (em km/l): "))
    
    carros.append(carro)
    consumo_gasolina.append(consumo)

    # Cálculo do consumo e custo para 500 km
    print("\nResultados:")

    for i in range(len(carros)):

        consumo_litros = distancia / consumo_gasolina[i]
        custo_total = consumo_litros * custo_gasolina
        
        print(f"\n{carros[i]}:")
        print(f"Consumo: {consumo_litros:.2f} litros")
        print(f"Custo: R$ {custo_total:.2f}")