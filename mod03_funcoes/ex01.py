def soma_tres_argumentos(a, b, c):
    # Calcula a soma dos três argumentos
    resultado = a + b + c
    return resultado

# Solicita ao usuário para inserir três números
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

# Chama a função e exibe o resultado
resultado_soma = soma_tres_argumentos(num1, num2, num3)
print(f"A soma dos três números é: {resultado_soma}")
