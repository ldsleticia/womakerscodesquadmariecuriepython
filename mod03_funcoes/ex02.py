def inverte_numero(numero):
    # Converte o número para uma string e inverte a ordem dos caracteres
    numero_invertido = str(numero)[::-1]
    
    # Converte o resultado de volta para um inteiro
    numero_invertido = int(numero_invertido)
    
    return numero_invertido

# Exemplo de uso:
numero_original = 127
numero_invertido = inverte_numero(numero_original)

print(f'O número invertido de {numero_original} é {numero_invertido}')