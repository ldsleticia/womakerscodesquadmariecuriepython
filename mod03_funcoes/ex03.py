#Exercício 3 Módulo 4

def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def menu():
    while True:
        print("\nMenu de Conversão de Temperatura")
        print("1 - Converter de Celsius para Fahrenheit")
        print("2 - Converter de Fahrenheit para Celsius")
        print("3 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            celsius = float(input("Digite a temperatura em Celsius: "))
            print(f"{celsius}°C é igual a {celsius_para_fahrenheit(celsius):.2f}°F")
        elif opcao == '2':
            fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
            print(f"{fahrenheit}°F é igual a {fahrenheit_para_celsius(fahrenheit):.2f}°C")
        elif opcao == '3':
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

menu()
