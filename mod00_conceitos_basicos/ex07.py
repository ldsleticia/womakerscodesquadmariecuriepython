# Solicite ao usuário o peso em kg e a altura em metros.Calcule e imprima o Índice de Massa Corporal(IMC) usando a fórmula:IMC=peso/(altura x altura).

# Solicita ao usuário o peso em kg e a altura em metros
peso = float(input("Digite o peso em kg: "))
altura = float(input("Digite a altura em metros: "))

# Calcula o Índice de Massa Corporal (IMC)
imc = peso / (altura ** 2)

# Imprime o resultado
print(f"O Índice de Massa Corporal (IMC) é: {imc:.2f}")
