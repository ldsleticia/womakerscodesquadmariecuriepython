#Exercício 6 Módulo 2

def verificar_acesso():
    while True:
        login = input("Digite o login: ")
        senha = input("Digite a senha: ")

        if login == "admin" and senha == "admin123":
            print("Acesso permitido.")
            break
        else:
            print("Erro: login ou senha incorretos. Tente novamente.")

verificar_acesso()
