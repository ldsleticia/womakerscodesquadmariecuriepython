"""
Crie uma função chamada contar_vogais que recebe uma string como parâmetro. 
Implemente a lógica para contar o número de vogais na string e retorne o 
total de vogais. Solicite ao usuário para inserir uma frase e utilize a função para contar as vogais
"""

def eh_vogal(letra):
    return letra in 'aeiouAEIOU'

def contar_vogais(mensagem):
    qtd_vogais = 0

    for caractere in mensagem:
        if eh_vogal(caractere):
            qtd_vogais += 1
    return qtd_vogais

mensagem = input("\nDigite sua frase: ")

print(contar_vogais(mensagem))