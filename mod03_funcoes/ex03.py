def troca_temperatura_para_celcius():
    temperatura = float(input('Digite a temperatura em Fahrenheit: '))
    conversao = (temperatura - 32) / 1.8
    print(f'{conversao:.1f}C')


def troca_temperatura_para_fahrenheit():
    temperatura = float(input('Digite a temperatura em Celsius: '))
    conversao = (temperatura * 1.8) + 32
    print(f'{conversao:.1f}F')


def menu():
    escolha = int(input('Digite sua opção, sendo 1 para converter para Celsius ou 2 para converter para Fahrenheit: '))
    match escolha:
        case 1:
            troca_temperatura_para_celcius()
        case 2:
            troca_temperatura_para_fahrenheit()


menu()
