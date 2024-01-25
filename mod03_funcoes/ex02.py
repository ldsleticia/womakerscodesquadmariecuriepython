#Exercício 2 Módulo 4

def reverso_numero(num):
    num_str = str(num)            # Converte o número para string
    num_str_reverso = num_str[::-1]  # Inverte a string
    return num_str_reverso   # Mantém como string

numero = input("Digite um número inteiro: ")
numero_reverso = reverso_numero(numero)
print("O reverso do número é:", numero_reverso)
