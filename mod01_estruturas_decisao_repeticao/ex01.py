#Exercício 1 Módulo 2

def imprimir_maior_numero():
    
    while True:
    
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
    
        if num1 > num2:
            print(f"O maior número é: {int(num1)}")
        elif num2 > num1:
            print(f"O maior número é: {int(num2)}")
        else:
            print("Os números são iguais.")


imprimir_maior_numero()
