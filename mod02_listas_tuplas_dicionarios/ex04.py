# Criação do dicionário de contatos
contatos = {
    'Debora': '123-456-7890',
    'Marilia': '987-654-3210',
    'Adriano': '555-123-4567',
    'Waldson': '999-888-7777'
}

# Solicita o nome do usuário a ser procurado
nome_procurado = input("Digite o nome do contato que deseja procurar: ")

# Verifica se o nome está no dicionário e imprime o resultado
if nome_procurado in contatos:
    print(f"Telefone de {nome_procurado}: {contatos[nome_procurado]}")
else:
    print(f"Contato de {nome_procurado} não encontrado.")