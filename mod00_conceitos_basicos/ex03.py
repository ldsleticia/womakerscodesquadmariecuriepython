# Função para converter quilômetros para metros, centímetros e milímetros
def converter_quilometros(kilometros):
    # 1 quilômetro é igual a 1000 metros
    metros = kilometros * 1000
    
    # 1 metro é igual a 100 centímetros
    centimetros = metros * 100
    
    # 1 metro é igual a 1000 milímetros
    milimetros = metros * 1000
    
    # Retornar os resultados
    return metros, centimetros, milimetros

# Pedir ao usuário a quantidade de quilômetros
quilometros = float(input("Digite a quantidade de quilômetros: "))

# Chamar a função para realizar as conversões
metros, centimetros, milimetros = converter_quilometros(quilometros)

# Exibir os resultados
print(f"{quilometros} quilômetros equivalem a:")
print(f"{metros} metros")
print(f"{centimetros} centímetros")
print(f"{milimetros} milímetros")

