# Faça um programa que lê três números inteiros e os mostra em ordem crescente.

numero = []
numero.append(int(input('Digite o primeiro número inteiro: '))) 
numero.append(int(input('Digite o segundo número inteiro: '))) 
numero.append(int(input('Digite o terceiro número inteiro: '))) 

numero.sort()

print(f'Ordem crescente dos números: {numero}')