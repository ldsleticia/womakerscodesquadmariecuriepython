"""
Criar um programa em Python que solicite três números ao usuário, 
utilize estruturas condicionais para determinar o maior entre 
eles e apresente o resultado.
"""

num1 = float(input("\nDigite o primeiro número: "))
num2 = float(input("\nDigite o segundo número: "))
num3 = float(input("\nDigite o terceiro número: "))

maior_num = ''

if num1 > num2:
    if num1 > num3:
        maior_num = num1
    else:
        maior_num = num3
elif num2 > num3:
    maior_num = num2
else:
    maior_num = num3

print(f'\nO maior valor eh: {maior_num}')
