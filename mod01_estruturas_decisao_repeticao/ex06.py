usuario = input("Digite o nome de usuário: ")
senha = input("Digite a senha: ")

usuario_de_acesso = "admin"
senha_de_acesso = "admin123"

if usuario == usuario_de_acesso and senha == senha_de_acesso:
    print('Acesso concedido!')
else:
    print('Acesso negado!')
