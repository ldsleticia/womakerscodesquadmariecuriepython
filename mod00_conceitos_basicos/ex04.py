litros_consumidos = int(input('Digite quantos litros de combustivel foram consumidos: '))
quilometros_percorridos = int(input('Digite quantos quilometros foram percorridos: '))

consumo_medio = quilometros_percorridos / litros_consumidos

print(f'Com base nos dados fornecidos, o consumo médio de combustível foi de {consumo_medio:.2f} km/l')
