# TODO: implementar
# Exercício Resolvido

# Peça ao usuário a quantidade de litros de combustível consumidos
litros_consumidos = float(input("Digite a quantidade de litros de combustível consumidos: "))

# Distância percorrida em quilômetros pelo usuário
distancia_percorrida = float(input("Digite a distância percorrida em quilômetros: "))

# Médio em km/l
consumo_medio = distancia_percorrida / litros_consumidos

# Imprime o resultado
print(f"O consumo médio é de {consumo_medio:.2f} km/l.")