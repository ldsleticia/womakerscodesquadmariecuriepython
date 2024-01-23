def numero_reverso():
    numero_a_reverter = int(input('Insira aqui o número a ser revertido: '))
    numero_revertido = str(numero_a_reverter)[::-1]
    print(f'O número revertido é {numero_revertido}')


numero_reverso()
